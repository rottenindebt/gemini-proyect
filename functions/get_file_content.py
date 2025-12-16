import os
from constants import MAX_CHARS

def get_file_content(working_directory, file_path):
    list_of_value = []

    test_dir = os.path.abspath(working_directory)
    objective = os.path.normpath(os.path.join(test_dir, file_path))
    tittle = f'===Content of *{file_path}* file==='
    separador = "\n---------------------------------------------------------------------------------\n"

    list_of_value.append('=' * len(tittle))
    list_of_value.append(tittle)
    list_of_value.append('=' * len(tittle) + "\n")

    valid_target_dir = os.path.commonpath([test_dir, objective]) == test_dir
    if not valid_target_dir:
        list_of_value.append(f'Error: Cannot read "{file_path}" as it is outside the permitted working directory')
        list_of_value.append(separador)
        return "\n".join(list_of_value)
        
    if not os.path.isfile(objective):
        list_of_value.append(f'Error: File not found or is not a regular file: "{file_path}"')
        list_of_value.append(separador)
        return "\n".join(list_of_value)
        
    with open(objective, "r") as file:
        file_content_string = file.read(MAX_CHARS)
        list_of_value.append(file_content_string)
        if len(file_content_string) == MAX_CHARS:
            list_of_value.append(f'[...File "{file_path}" truncated at {MAX_CHARS} characters]')

        list_of_value.append(separador)

    return "\n".join(list_of_value)
            
