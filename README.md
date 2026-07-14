# Informe Técnico Caso Counter Strike Global Offensive

## Descripción

Proyecto desarrollado para aplicar técnicas de Machine Learning sobre datos de rondas competitivas de CS:GO. El sistema contiene dos modelos predictivos:
- Un modelo de clasificación basado en Random Forest para predecir el equipo ganador de una ronda.
- Un modelo de regresión basado en Support Vector Regression para estimar el tiempo promedio de supervivencia de los jugadores durante una ronda.

Los modelos fueron entrenados y evaluados en un Jupyter Notebook y posteriormente serializados para ser consumidos mediante una API desarrollada con Flask.
Se utilizó el método CRISP-DM para la realización de este trabajo, se incluyeron las siguientes etapas.

1. Exploración y preparación de los datos.
2. Transformación de los registros a nivel de ronda.
3. Entrenamiento y evaluación de modelos.
4. Selección de los modelos con mejor desempeño.
5. Serialización de los modelos entrenados.
6. Implementación de una API con Flask.
7. Consumo de los modelos desde una interfaz web.

## Estructura del proyecto

```
INFORME_TECNICO_CS-GO/
├── app.py
├── model/
│   ├── model_train_randomforest_classifier.joblib
│   └── model_train_svr_regressor.joblib
├── notebooks/
│   └── Informe_Tecnico_FMY0100_VFINAL.ipynb
├── templates/
│   ├── index.html
│   └── result.html
├── static/
│   └── style.css
├── requirements.txt
├── README.md
└── .gitignore

```

## Instalación del proyecto

### 1. Clonar repo
```
git clone https://github.com/paufriasest/Informe_Tecnico_CS-GO
cd INFORME_TECNICO_CS-GO
```

### 2. Crear EnVir
```
python -m venv venv
```

### 3. Activar el entorno
```
.\venv\Scripts\Activate.ps1
```

### 4. Instalar dep
```
pip install -r requirements.txt
```

## Ejecución local

Levantar app con Flask.
```
python app.py
```
Disponible en el URL
```
http://127.0.0.1:5000

```


---

## Autores
- Sebastián Valdivia
- Paula Frías

```
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⠶⠶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⣀⣿⠁⠀⠀⢹⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣀⠀⠀⠀⠀⣀⣤⠴⠖⠛⠛⠋⠉⠉⠉⠙⠋⠀⠀⠀⠘⠁⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⡴⠛⠉⠛⣦⣴⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠛⠳⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠸⡇⠀⠀⠀⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣹⡦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣸⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢀⡾⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡆⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢠⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠐⠛⠳⠆⠀⠀⠀⠀⠀⠀⠀⢠⣾⠛⢳⣆⠀⠀⠄⠐⡀⣄⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀
⠀⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣄⡀⠀⠀⠀⠀⠀⠀⠸⣿⣷⣻⡟⠈⡆⣸⢸⡇⠃⣁⡀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀
⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣁⣼⣿⠀⠀⠀⠀⠀⠀⠀⠀⠉⠁⠘⡀⠁⢈⣤⡴⠋⠉⠉⠙⢦⣀⣿⠀⠀⠀⠀⠀⠀⠀⠀
⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠠⠄⠀⠻⠷⠾⠋⠀⠀⡀⠀⣶⣀⡶⠀⠀⠀⠀⢀⣰⠏⠀⣠⡴⠶⠶⣦⡈⢿⣿⠳⣆⠀⠀⠀⠀⠀⠀
⠘⣇⠀⠀⠀⠀⠀⠀⡐⡇⣴⢠⡆⡖⠀⠀⠀⣀⡀⠟⠟⢋⢉⡀⠀⠀⠀⢀⡿⠁⢀⡾⠋⠀⠙⢳⣄⠙⢷⡈⠳⠿⢤⣤⡀⠀⠀⠀
⠀⢿⡄⠀⠀⠀⠀⠀⠻⠇⠙⠈⠁⠠⠊⠀⠘⠤⠗⠀⠀⠈⠉⣠⠤⠶⠛⠉⠀⣠⡞⠀⠀⠀⠀⠀⠙⣆⠈⢷⡀⠠⠀⠀⠙⣦⡀⠀
⠀⠘⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡁⠀⣴⠟⠋⠉⠉⠀⠀⠀⠀⠀⠀⠀⢸⡆⠘⠷⢦⣤⡈⠂⠹⣧⡀
⠀⠀⠈⢿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣧⠀⢿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠓⠒⠳⣦⢹⡆⠀⠈⣷
⠀⠀⠀⠀⠙⢷⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣤⠶⠷⣦⠈⢷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⢏⣼⠃⠀⢠⡟
⠀⠀⠀⠀⠀⠀⠀⠉⢫⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⡟⠀⢨⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡶⠋⣡⡟⠁⠀⢀⣼⠁
⠀⠀⠀⠀⠀⠀⠀⠀⠈⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢸⡇⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⣿⠀⠀⣴⠋⠁⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠸⣆⠀⠀⠀⢀⣠⡤⢦⣀⠀⠀⢠⡿⠀⡟⠀⢠⡏⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠘⣧⠀⢹⣧⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢷⣄⠀⠉⠛⠛⢛⠏⢁⣀⠀⠙⠳⢦⣤⣤⠞⠁⠀⣸⠇⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠀⠙⠳⠦⣤⡄⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠒⢒⡖⠚⠚⠋⠉⠛⢦⣤⣀⣀⣀⣀⣤⠾⠋⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⡀⠀⢸⡗⠒⠶⠶⠒⢶⡆⢀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠒⠛⠁⠀⠀⠀⠀⠈⠛⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
```