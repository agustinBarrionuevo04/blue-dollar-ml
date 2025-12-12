# Conclusiones del Análisis Exploratorio (EDA)

Tras procesar la serie histórica del Dólar Blue, hemos identificado las siguientes características estadísticas clave:

### 1. Tendencia y Estacionariedad
* **Crecimiento Exponencial:** La serie de precios (`valor`) muestra una tendencia alcista agresiva y no lineal. El gráfico en escala logarítmica revela que la depreciación del peso es constante desde el inicio de la serie, no solo en los últimos años.
* **No es Estacionaria:** La media y la varianza del precio cambian drásticamente con el tiempo. Esto implica que no podemos usar el precio bruto para modelos predictivos simples sin antes transformarlo.

### 2. Análisis de Retornos (Volatilidad)
Al derivar la serie (`pct_change`), transformamos el precio en **retornos diarios**, observando que:
* **Oscilación en torno a cero:** A diferencia del precio, los retornos sí parecen estacionarios (se mueven alrededor del 0%).
* **Volatilidad Agrupada (Clustering):** La volatilidad no es constante. Hay periodos de calma seguidos de "estallidos" violentos de varianza (crisis cambiarias), visibles claramente en los picos del gráfico de variaciones.

### 3. Distribución y Outliers ("Colas Gordas")
El análisis de histogramas y boxplots confirma que los datos financieros argentinos no siguen una distribución normal perfecta:
* **Asimetría a la Derecha (Right Skew):** El histograma tiene una "cola" larga hacia la derecha. Esto confirma que las variaciones bruscas son casi siempre subidas de precio (devaluaciones), y rara vez bajadas.
* **Colas Gordas (Fat Tails):** El Boxplot muestra una cantidad masiva de *outliers* (círculos negros). Esto indica que los "eventos extremos" (subidas mayores al 5% o 10% diario) son mucho más frecuentes de lo que la estadística tradicional predeciría. Estos outliers coinciden con eventos históricos de crisis (2002, 2018, etc.).

### 4. Suavizado
* La aplicación de **Medias Móviles (`rolling`)** permite filtrar el ruido diario y visualizar la tendencia subyacente de corto y mediano plazo, facilitando la identificación de cambios de tendencia reales frente a la especulación diaria.