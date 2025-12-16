import os

def get_files_info(working_directory, directory="."):
    list_of_value = []
    file_name = directory
    separador = "\n---------------------------------------------------------------------------------\n"

    test_dir = os.path.abspath(working_directory)
    objective = os.path.normpath(os.path.join(test_dir, directory))

    if directory == ".":
        file_name = "current"

    tittle = f"===Result for {file_name} directory:==="
    list_of_value.append("=" * len(tittle))
    list_of_value.append(tittle)
    list_of_value.append("=" * len(tittle) + '\n')

    if not os.path.isdir(objective):
        list_of_value.append(f'Error: "{directory}" is not a directory')
        return "\n".join(list_of_value) + separador

    valid_target_dir = os.path.commonpath([test_dir, objective]) == test_dir
    if not valid_target_dir: 
        list_of_value.append(f'Error: Cannot list "{directory}" as it is outside the permitted working directory')
        return "\n".join(list_of_value) + separador


    for item in os.listdir(objective):
        object_path = os.path.join(objective, item)
        list_of_value.append(f" - {item}: file_zize={os.path.getsize(object_path)} is_dir={os.path.isdir(object_path)} ")

    return "\n".join(list_of_value) + separador


