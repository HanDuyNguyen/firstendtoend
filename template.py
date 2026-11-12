import os
from pathlib import Path
import logging

project_name = "mlendtoend"

list_of_files = [
    ".github/workflows/ci.yaml",
    f"src/{project_name}/__init__",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "Dockerfile"
    "setup.py",
    "research/research.ipynb",
    "templates/index.html"
]

for file_path in list_of_files:
    file_path = Path(file_path)
    file_dir = file_path.parent

    if file_dir != "":
        os.makedirs(file_dir, exist_ok=True)

    if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
        with open(file_path, "w") as f:
            pass
