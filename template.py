import os
from pathlib import Path

root = "src"

list_of_files = [

    f"{root}/__init__.py",
    f"{root}/components/__init__.py",
    f"{root}/components/data_ingestion.py",  
    f"{root}/components/data_validation.py",
    f"{root}/components/data_transformation.py",
    f"{root}/components/model_trainer.py",
    f"{root}/components/model_evaluation.py",
    f"{root}/components/model_pusher.py",
    f"{root}/configuration/__init__.py",
    f"{root}/configuration/mongo_db_connection.py",
    f"{root}/configuration/aws_connection.py",
    f"{root}/cloud_storage/__init__.py",
    f"{root}/cloud_storage/aws_storage.py",
    f"{root}/data_access/__init__.py",
    f"{root}/data_access/proj1_data.py",
    f"{root}/constants/__init__.py",
    f"{root}/entity/__init__.py",
    f"{root}/entity/config_entity.py",
    f"{root}/entity/artifact_entity.py",
    f"{root}/entity/estimator.py",
    f"{root}/entity/s3_estimator.py",
    f"{root}/exception/__init__.py",
    f"{root}/logger/__init__.py",
    f"{root}/pipline/__init__.py",
    f"{root}/pipline/training_pipeline.py",
    f"{root}/pipline/prediction_pipeline.py",
    f"{root}/utils/__init__.py",
    f"{root}/utils/main_utils.py",
    "app.py",
    "requirements.txt",
    "Dockerfile",
    ".dockerignore",
    "demo.py",
    "setup.py",
    "pyproject.toml",
    "config/model.yaml",
    "config/schema.yaml",
]

for filepath in list_of_files:
    filepath = Path(filepath)

    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass

    else:
        print(f"file is already present at : {filepath}")