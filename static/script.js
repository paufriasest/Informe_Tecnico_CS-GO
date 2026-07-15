let btnModels = document.querySelector(".btnsModels");
let btnRegression = document.getElementById("btnRegression");
let btnClasiffication = document.getElementById("btnClasiffication");

let formModel = document.getElementById("form");
let params = document.getElementById("params");
let btnPredict = document.getElementById("btnPredict");
let containerResult = document.getElementById("containerResult");

const resultado = document.getElementById("resultado");

let selectedModel = null;

function showForm(model) {
  selectedModel = model;

  btnRegression.style.display = "none";
  btnClasiffication.style.display = "none";

  formModel.style.display = "flex";
  containerResult.style.display = "none";

  resultado.textContent = "";
}

btnRegression.addEventListener("click", () => {
  showForm("regression");
});

btnClasiffication.addEventListener("click", () => {
  showForm("classification");
});

btnPredict.addEventListener("click", onClickPredictBtn);

async function onClickPredictBtn() {
  let formdata = params.value.trim();

  if (!formdata) {
    alert("Ingresar parametros en formato JSON");
    return;
  }

  let payload = JSON.parse(formdata);

  let endpoint;

  if (selectedModel == "regression") {
    endpoint = "/api/predict/regressor";
  } else {
    endpoint = "/api/predict/clasiffier";
  }

  try {
    const res = await axios.post(endpoint, payload);

    formModel.style.display = "none";
    containerResult.style.display = "flex";

    document.getElementById("resultado").innerHTML += res.data.prediction;
    if (selectedModel === "regression") {
      resultado.textContent =
        `Tiempo promedio estimado: ` + `${res.data.prediction} segundos`;
    } else {
      resultado.textContent =
        `Predicción: ` +
        `${res.data.predicted_class} `;
    }

    params.value = "";
  } catch (error) {
    console.error("Error:", error);
    const serverMessage =
      error.response?.data?.error ||
      error.response?.data?.detail ||
      "No fue posible generar la predicción.";

    resultado.textContent = serverMessage;

    formModel.style.display = "none";
    containerResult.style.display = "flex";
  }
}
