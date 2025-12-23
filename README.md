# Blue Dollar ML

Conjunto de utilidades para preparar datos históricos del dólar blue y
entrenar modelos supervisados sencillos que predicen si el precio subirá
al día siguiente.

## Estructura de directorios

```
blue-dollar-ml/
├── data/                # Archivos raw y procesados generados por los pipelines
├── docs/
├── notebooks/           # Exploración y prototipos
├── src/
│   └── blue_dollar_ml/
│       ├── config.py
│       ├── data_processing/
│       ├── features/
│       ├── models/
│       └── pipelines/
└── requirements.txt
```

El paquete `blue_dollar_ml` encapsula toda la lógica de negocio y expone
funciones reutilizables para notebooks, scripts o tests.

## Preparación del entorno

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Todas las ejecuciones de Python deben declarar `PYTHONPATH=src` para que
el paquete local quede disponible.

## Pipelines principales

```bash
# Limpiar fechas, ordenar datos crudos y concatenar CSV
PYTHONPATH=src python -m blue_dollar_ml.pipelines.prepare_data

# Entrenar los modelos (Regresión Logística y Random Forest)
PYTHONPATH=src python -m blue_dollar_ml.pipelines.train_models
```

Cada modelo imprime su exactitud final y puede reutilizarse desde un
notebook importando `train_logistic_regression` o `train_random_forest`.

## Comentarios finales

- Las rutas de archivos viven en `blue_dollar_ml.config`, evitando paths
  absolutos en el código.
- El paquete está modularizado (data processing, models y pipelines) para
  simplificar futuras ampliaciones o pruebas automatizadas.
- Añade tus propios pipelines dentro de `src/blue_dollar_ml/pipelines/`
  siguiendo el patrón existente si necesitas flujos adicionales.
