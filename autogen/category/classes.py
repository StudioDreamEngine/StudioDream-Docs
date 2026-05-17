import yaml
import pathlib as path
import os
import shutil

global icons_path
icons_path = path.Path(".") / "docs" / "theme"/ ".icons" / "studiodream"

def generate(source: path.Path, target: path.Path):
    classes = {}
    inherited_by = {}

    # Pass 1
    for file in os.listdir(source):
        file_path = source / file
        print(file)
        file_yaml = yaml.load(open(file_path), Loader=yaml.FullLoader)

        classes.update({file_path.stem: file_yaml})

        if "BaseType" in file_yaml.keys():
            if not (file_yaml["BaseType"] in inherited_by.keys()):
                inherited_by.update({file_yaml["BaseType"]: []})

            inherited_by[file_yaml["BaseType"]].append(file_path.stem)

    print("Finish pass 1")

    # Pass 2
    for file in os.listdir(source):
        # Setup some stuff
        file_path = source / file
        print(file)
        file_yaml = classes[file_path.stem]

        target_path = target / file
        if "Category" in file_yaml.keys(): target_path = target / file_yaml["Category"] / file

        name = file_yaml["Name"]

        emoji_exists = (icons_path / (name + ".svg")).exists()
        emoji = (emoji_exists and name or "Unknown")

        # Start creating the md file
        mk = ""
        def append_line(line): nonlocal mk; mk += line+"\n" # Fucking dumbassery

        def get_default(dict, key, default=False):
            return (key in dict.keys()) and dict[key] or default

        def add_flags(prop):
            flags = []

            if get_default(prop, "IsAccessible"): flags.append("Accessible")
            if get_default(prop, "IsSerialized"): flags.append("Serialized")
            if get_default(prop, "IsInternal"): flags.append("Internal")
            if get_default(prop, "ReadOnly"): flags.append("ReadOnly")

            return f"``{"`` ``".join(flags)}``"
        
        append_line("---")
        append_line("title: " + name)
        append_line("description:")
        append_line("icon: studiodream/"+emoji)
        append_line("---")
        append_line("")
        append_line(f"# :studiodream-{emoji}: {name}")

        if "BaseType" in file_yaml.keys():
            append_line("")
            append_line(f"{{{{ inherits(\"{file_yaml["BaseType"]}\") }}}}")

        children: list = get_default(inherited_by, name, None)
    
        if children and len(children) > 0:
            append_line("")
            append_line(f"{{{{ inherited_by([\"{"\", \"".join(children)}\"]) }}}}")

        append_line("")
        append_line(file_yaml["Description"])
        append_line("")

        if get_default(file_yaml, "IsAbstract"):
            append_line("{{ abstract() }}")
            append_line("")

        if not get_default(file_yaml, "IsCreatable"):
            append_line("{{ notnewable() }}")
            append_line("")

        properties = ("Properties" in file_yaml) and file_yaml["Properties"] or []

        if len(properties) > 0:
            append_line("")
            append_line("## Properties")
            append_line("")

        for prop in properties:
            type = get_default(prop, "Type", "void")

            append_line(f"### {prop["Name"]}:{type} {{ property }}")
            append_line(add_flags(prop))
            append_line("")
            append_line(get_default(prop, "Description", f"The {prop["Name"]} of this object."))
            append_line("")

        methods = ("Methods" in file_yaml) and file_yaml["Methods"] or []

        if len(methods) > 0:
            append_line("")
            append_line("## Methods")
            append_line("")

        for method in methods:
            parameters = get_default(method, "Parameters", [])
            return_type = get_default(method, "ReturnType", "void")
            params = []

            for param in parameters:
                optional = get_default(param, "IsOptional")

                params.append(f"{param["Name"]};{param["Type"]}{optional and "?" or ""}")

            method["IsAccessible"] = True

            append_line(f"### {method["Name"]}({",".join(params)}):{return_type} {{ method }}")
            append_line(add_flags(method))
            append_line("")
            append_line(get_default(method, "Description", "Missing Documentation!"))
            append_line("")

        # TODO: Events

        #print(mk)

        parent_path = target_path.parent 

        if not parent_path.exists():
            os.makedirs(target_path.parent)

        open(parent_path/(target_path.stem+".md"), "w").write(mk)