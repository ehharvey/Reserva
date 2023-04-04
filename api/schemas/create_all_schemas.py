from pathlib import Path
import yaml
from pydantic import BaseModel, Field
import os

# get the directory path of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# set the working directory to be the script directory
os.chdir(script_dir)

class RefModel(BaseModel):
    ref: str = Field(..., alias="$ref")

folders = [
    Path("authentication"),
    Path("credit"),
    Path("group"),
    Path("item"),
    Path("unavailability"),
    Path("user"),
    Path("meta")
]

boilerplate = """---
# DO NOT MODIFY THIS FILE BY HAND
# IT IS AUTO GENERATED BY create_all_schemas.py
"""

all_adjusted_output = {}

with open("_all.yaml", "w") as output:
    output.write(boilerplate)

    for folder in folders:
        for file in folder.iterdir() if folder.is_dir() else []:
            if file.name != "_index.yaml":
                continue
            else:
                with open(file, "r") as file:
                    for key, value in yaml.safe_load(file).items():
                        ref_model = RefModel(**value)

                        all_adjusted_output[key] = {
                            "$ref": f"./{folder.name}/{Path(ref_model.ref)}"
                        }

    output.write(yaml.dump(all_adjusted_output))
