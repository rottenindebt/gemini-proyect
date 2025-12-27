import os
import subprocess

def run_python_file(working_directory, file_path, args=None):
    list_of_value = []

    try:
        test_dir = os.path.abspath(working_directory)
        objective = os.path.normpath(os.path.join(test_dir, file_path))
        separador = "\n" + ("-" * 45) + "\n"
        tittle = f'=== Trying to run "{file_path}" ==='

        list_of_value.append('=' * len(tittle))
        list_of_value.append(tittle)
        list_of_value.append('=' * len(tittle))

        valid_test_dir = os.path.commonpath([ test_dir, objective ]) == test_dir
        if not valid_test_dir:
            list_of_value.append(f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory')
            list_of_value.append(separador)
            return "\n".join(list_of_value)

        if not os.path.isfile(objective):
            list_of_value.append(f'Error: "{file_path}" does not exist or is not a regular file')
            list_of_value.append(separador)
            return "\n".join(list_of_value)

        if not file_path.endswith(".py"):
            list_of_value.append(f'Error: "{file_path}" is not a Python file')
            list_of_value.append(separador)
            return "\n".join(list_of_value)

        command = [ "python", objective ]
        if args != None:
            command.extend(args)

        accion = subprocess.run(command, text=True, timeout=30.0, capture_output=True)

        if accion.stdout != None or accion.stderr != None:
            list_of_value.append('STDOUT:' + f'\n{accion.stdout}')
            list_of_value.append('STDERR:' + f'\n{accion.stderr}')
        else:
            list_of_value.append('No output produced')

        if accion.returncode != 0:
            list_of_value.append(f'Process exited with code {accion.returncode}')

        list_of_value.append(separador)

        return "\n".join(list_of_value)

    except Exception as e:
        return f"Error: executing Python file: {e}"
        
