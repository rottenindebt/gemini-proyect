import os
import sys

def get_files_info(working_directory, directory="."):

    test_dir = os.path.abspath(working_directory)
    objective = os.path.normpath(os.path.join(test_dir, directory))


    if not os.path.isdir(objective):
        print(f'Error: "{directory}" is not a directory')
        return

    valid_target_dir = os.path.commonpath([test_dir, objective]) == test_dir
    if not valid_target_dir: 
        print(f'Error: Cannot list "{directory}" as it is outside the permitted working directory')
        return

    if directory == ".":
        directory = "current"
    print(f"Result for {directory} directory:")

    for item in os.listdir(objective):
        object_path = os.path.join(objective, item)
        print(f" - {item}: file_zize={os.path.getsize(object_path)} is_dir={os.path.isdir(object_path)} ")


