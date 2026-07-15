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
## Parámetros de prueba

Para ocupar el modelo de regresión sugerimos ocupar:
```
{
  "AssaultRifle_CounterTerrorist": 2,
  "AssaultRifle_Terrorist": 4,
  "Assists_CounterTerrorist": 1,
  "Assists_Terrorist": 3,
  "AvgTravelledDistance": 85000,
  "EquipmentValue_CounterTerrorist": 3800,
  "EquipmentValue_Terrorist": 4300,
  "FirstKillTime": 32.5,
  "FlankKills_CounterTerrorist": 0,
  "FlankKills_Terrorist": 1,
  "Headshots_CounterTerrorist": 1,
  "Headshots_Terrorist": 3,
  "Heavy_CounterTerrorist": 0,
  "Heavy_Terrorist": 0,
  "Kills_CounterTerrorist": 2,
  "Kills_Terrorist": 5,
  "LethalGrenades_CounterTerrorist": 2,
  "LethalGrenades_Terrorist": 3,
  "Map_de_dust2": 0,
  "Map_de_inferno": 0,
  "Map_de_mirage": 1,
  "Map_de_nuke": 0,
  "NonLethalGrenades_CounterTerrorist": 4,
  "NonLethalGrenades_Terrorist": 6,
  "Pistol_CounterTerrorist": 2,
  "Pistol_Terrorist": 1,
  "SMG_CounterTerrorist": 1,
  "SMG_Terrorist": 0,
  "SniperRifle_CounterTerrorist": 1,
  "SniperRifle_Terrorist": 1,
  "TeamEquipmentValue_CounterTerrorist": 20500,
  "TeamEquipmentValue_Terrorist": 24000,
  "TotalGrenadesThrown": 15,
  "TotalRoundAssists": 4,
  "TotalRoundHeadshots": 4,
  "TotalRoundKills": 7
}

```

Y para ocupar el modelo de clasificación sugerimos ocupar:
```
{
  "AssaultRifle_CounterTerrorist": 4,
  "AssaultRifle_Terrorist": 2,
  "Assists_CounterTerrorist": 4,
  "Assists_Terrorist": 1,
  "AvgTimeAlive": 78.5,
  "AvgTravelledDistance": 92000,
  "EquipmentValue_CounterTerrorist": 4500,
  "EquipmentValue_Terrorist": 3500,
  "FirstKillTime": 27.8,
  "FlankKills_CounterTerrorist": 2,
  "FlankKills_Terrorist": 0,
  "Headshots_CounterTerrorist": 3,
  "Headshots_Terrorist": 1,
  "Heavy_CounterTerrorist": 0,
  "Heavy_Terrorist": 0,
  "Kills_CounterTerrorist": 5,
  "Kills_Terrorist": 2,
  "LethalGrenades_CounterTerrorist": 3,
  "LethalGrenades_Terrorist": 2,
  "Map_de_dust2": 0,
  "Map_de_inferno": 1,
  "Map_de_mirage": 0,
  "Map_de_nuke": 0,
  "NonLethalGrenades_CounterTerrorist": 7,
  "NonLethalGrenades_Terrorist": 4,
  "Pistol_CounterTerrorist": 1,
  "Pistol_Terrorist": 2,
  "SMG_CounterTerrorist": 0,
  "SMG_Terrorist": 1,
  "SniperRifle_CounterTerrorist": 1,
  "SniperRifle_Terrorist": 1,
  "TeamEquipmentValue_CounterTerrorist": 24500,
  "TeamEquipmentValue_Terrorist": 19000,
  "TotalGrenadesThrown": 16,
  "TotalRoundAssists": 5,
  "TotalRoundHeadshots": 4,
  "TotalRoundKills": 7
}

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