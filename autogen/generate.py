import pathlib as path
import shutil
import os


import category.classes as classes


source_path = path.Path(".") / "yaml"
target_path = path.Path(".") / "docs" / "api"



# Cleanup
for file in os.listdir(source_path):
    if (target_path / file).exists():
        shutil.rmtree(target_path / file)


# Create Directories
for category in os.listdir(source_path):
    os.mkdir(target_path / category)


# Generate 
classes.generate(source_path / "classes", target_path / "classes")
classes.generate(source_path / "types", target_path / "types")
classes.generate(source_path / "services", target_path / "services")
#classes.generate(source_path / "runtime", target_path / "runtime")