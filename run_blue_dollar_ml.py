"""
Tiny helper script that runs the preprocessing and training pipelines.
"""

import os
import subprocess
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent


def _run_pipeline(module: str) -> None:
    env = os.environ.copy()
    env["PYTHONPATH"] = str(PROJECT_ROOT / "src")
    print(f"\n==> Ejecutando {module}")
    subprocess.run(
        [sys.executable, "-m", module],
        check=True,
        cwd=PROJECT_ROOT,
        env=env,
    )


def main() -> None:
    _run_pipeline("blue_dollar_ml.pipelines.prepare_data")
    _run_pipeline("blue_dollar_ml.pipelines.train_models")


main()
