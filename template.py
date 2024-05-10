import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name="cnnClassifier"

list_of_files=[
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/configuartion.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "dvc.yaml",
    "setup.py",
    "requirements.txt",
    "research/trials.ipynb"
]

for directory in list_of_files:
    filepath=Path(directory)
    filedir, filename=os.path.split(filepath)

    if filedir !='':
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Created directory {filedir}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath, "w") as f:
            pass
        logging.info(f"Empty file {filepath} created.")

    else:
        logging.info(f"{filepath} already exist.")
    