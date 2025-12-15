# Definición del Problema de Machine Learning

## 1. Objetivo
Predecir la dirección del movimiento del Dólar Blue para el día siguiente.
* **Tipo de Problema:** Clasificación Binaria
* **Horizonte:** t+1 (Un día hacia adelante).

## 2. Variables
* **Target ($y$):** `target_up`.
    * 1: Si el retorno diario > 0 (El precio sube).
    * 0: Si el retorno diario <= 0 (El precio baja o se mantiene).
* **Features ($X$):**
    * `lag_1`: El retorno del día anterior. (Hipótesis: Si ayer subió mucho, hoy quizás corrige).

## 3. Estrategia de Validación (Split)
Dado que es una serie temporal, no usaremos validación aleatoria (shuffle). Se respeta el orden cronológico:
* **Train (70%):** Datos más antiguos para entrenar.
* **Validation (15%):** Datos intermedios para ajustar hiperparámetros.
* **Test (15%):** Datos más recientes para la evaluación final.