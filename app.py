import joblib
import numpy as np
import pandas as pd
from flask import Flask, jsonify, render_template, request

#levantar Flask
app = Flask(__name__)

# Cargar los modelos
regression_artifact = joblib.load(
    "model/model_train_svr_regressor.joblib"
)

svr_model = regression_artifact["model"]
svr_features = regression_artifact["features"]


classification_artifact = joblib.load(
    "model/model_train_randomforest_classifier.joblib"
)

classification_model = classification_artifact["model"]
classification_features = classification_artifact["features"]

def expected_data(data, expected_features):
    missing_features = []
    
    for feature in expected_features:
        if feature not in data:
            missing_features.append(feature)
    
    if missing_features:
        raise ValueError(
            "Faltan variables" + missing_features
        )
    
    ordered_data = {}
    
    for feature in expected_features:
        ordered_data[feature] = data[feature]
    
    return pd.DataFrame([ordered_data])

@app.route("/")
def index():
    return render_template("index.html")

@app.get("/health")
def health():
    return jsonify({
        "status": "ok",
        "models": {
            "classification": "loaded",
            "regression": "loaded"
        }
    })

# Clasificacion
@app.post("/api/predict/clasiffier")
def predict_clasfication():
    
    data = request.get_json()
    
    if not data:
        return jsonify({
            "error": "Se necesitan los datos en json",
        }), 400
        
    input_data = expected_data(data, classification_features)
    
    prediction = int(classification_model.predict(input_data)[0])
    
    probabilities = (classification_model.predict_proba(input_data)[0])
    
    class_names = classification_artifact.get(
        "class_names",
        {
            0: "Counter-Terrorist",
            1: "Terrorist"
        }
    )
    
    return jsonify({
        "model": "Random Forest Classifier",
        "target": "RoundWinner",
        "prediction": prediction,
        "predicted_class": class_names[prediction],
        "probabilities": {
            "Counter-Terrorist": round(
                float(probabilities[0]),
                4
                ),
            "Terrorist": round(
                float(probabilities[1]),
                4
            )
        }
    })

# Regresion
@app.post("/api/predict/regressor")
def predict_regression():
    
    data = request.get_json()
    
    if not data:
        return jsonify({
            "error": "Se necesitan los datos en json",
        }), 400
        
    input_data = expected_data(data, svr_features)
    
    prediction = int(svr_model.predict(input_data)[0])
    
    prediction = max(15, min(155, prediction))
    
    return jsonify({
        "model": "Support Vector Regression",
        "target": "AvgTimeAlive",
        "prediction": round(prediction, 2),
        "unit": "seconds"
    })


@app.get("/api/features/classification")
def get_classification_features():
    return jsonify({
        "features": classification_features
    })


@app.get("/api/features/regression")
def get_regression_features():
    return jsonify({
        "features": svr_features
    })

if __name__ == "__main__":
    app.run(debug=True)
