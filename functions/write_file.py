import os

def write_file(working_directory, file_path, content):
    list_of_value = []
    file_name = file_path
    separador = "\n---------------------------------------------------------------------------------\n"

    test_dir = os.path.abspath(working_directory)
    objective = os.path.normpath(os.path.join(test_dir, file_path))

    if file_path == ".":
        file_name = "current"

    tittle = f"=== Wirting in the *{file_name}* file ==="
    list_of_value.append("=" * len(tittle))
    list_of_value.append(tittle)
    list_of_value.append("=" * len(tittle) + '\n')

    if os.path.isdir(objective):
        list_of_value.append(f'Error: Cannot write to "{file_name}" as it is a directory')
        return "\n".join(list_of_value) + separador

    valid_target_dir = os.path.commonpath([test_dir, objective]) == test_dir
    if not valid_target_dir: 
        list_of_value.append(f'Error: Cannot write to "{file_name}" as it is outside the permitted working directory')
        return "\n".join(list_of_value) + separador

    os.makedirs(os.path.dirname(objective), exist_ok=True)
    with open(objective, "w") as file:
        file.write(content)
        list_of_value.append(f'Successfully wrote to "{file_path} ({len(content)} characters written)"')
        return "\n".join(list_of_value) + separador

    
