# Predicción del Dólar Blue con Machine Learning

Este proyecto aplica técnicas de **Machine Learning** para predecir la dirección diaria (Sube/Baja) del Dólar Blue en Argentina.

A diferencia de los modelos tradicionales de series de tiempo, este enfoque utiliza un **Random Forest Classifier** alimentado por indicadores técnicos y variables macroeconómicas clave (como la Brecha Cambiaria), logrando superar significativamente al azar y a las estrategias básicas de "Buy & Hold".

---

## 🚀 Resultados Destacados

* **Accuracy Final:** `68.47%` (Random Forest).
* **Benchmark (Azar/Mayoría):** ~58%.
* **Mejora:** El modelo final demostró capacidad para detectar patrones no lineales en un mercado altamente volátil e inflacionario.

---

## 🧠 La Evolución del Proyecto (Metodología)

El desarrollo no fue lineal. Se iteró a través de varias fases para resolver problemas complejos inherentes a la economía argentina:

### 1. Fase Inicial: Regresión Logística & Lags

* **Enfoque:** Usar el precio de ayer para predecir el de mañana.
* **Problema:** El modelo apenas superaba el 50% (azar). Sufría de **Data Leakage** (fugas de información) al usar promedios móviles mal calculados.

### 2. El Desafío de la Inflación (No-Estacionariedad)

* **Obstáculo:** Al usar precios nominales (pesos), el modelo falló catastróficamente (34% de accuracy) cuando se probó en datos nuevos con precios mucho más altos. Aprendió reglas como *"Si vale más de $100, baja"*, que quedaron obsoletas por la inflación.
* **Solución:** Se transformaron todas las variables a **Retornos Logarítmicos y Variaciones Porcentuales**. El modelo dejó de mirar "precios" y empezó a mirar "comportamientos".

### 3. Ingeniería de Features (El "Secreto")

Para romper el techo del 58%, se incorporaron variables financieras avanzadas:

* **Brecha Cambiaria:** La diferencia porcentual entre el Dólar Oficial y el Blue. (Factor predictor #1).
* **RSI (Relative Strength Index):** Para detectar sobrecompra/sobreventa.
* **Estacionalidad:** Días de la semana y efectos de fin de mes.

---

## 🛠️ Stack Tecnológico

* **Lenguaje:** Python
* **Manejo de Datos:** Pandas, NumPy
* **Modelado:** Scikit-learn (RandomForestClassifier, LogisticRegression)
* **Visualización:** Matplotlib
* **Validación:** TimeSeriesSplit (para respetar la cronología)

---

## 📂 Estructura del Proyecto

```bash
├── data/
│   ├── raw/                  # Datos crudos (CSV originales)
│   └── processed/            # Datos limpios y features calculados (features_advanced.csv)
├── notebooks/
│   ├── 01_eda.ipynb          # Análisis Exploratorio de Datos
│   ├── 02_features.ipynb     # Creación de RSI, Brecha y Lags
│   └── 03_ml_models.ipynb    # Entrenamiento, GridSearch y Backtesting
├── src/                      # Scripts 
└── README.md

```

## 📊 Visualización del Backtesting

El modelo fue sometido a una simulación de inversión (Backtesting) en el conjunto de prueba (datos no vistos por el modelo).

![alt text](image.png)

> **Conclusión del Backtesting:** La estrategia basada en Random Forest logró capitalizar las correcciones del mercado gracias a la lectura de la "Brecha", evitando caídas y superando la estrategia pasiva de mantener dólares.

---

## 🔧 Instalación y Uso

1. Clonar el repositorio:
```bash
git clone https://github.com/agustinBarrionuevo04/blue-dollar-ml.git

```


2. Instalar dependencias:
```bash
pip install -r requirements.txt

```


3. Ejecutar los notebooks en orden para reproducir el proceso de entrenamiento.

---

**Autor:** Agustin Barrionuevo - Estudiante de Cs. de la Computación.
