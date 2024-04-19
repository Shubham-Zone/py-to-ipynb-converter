import os
import nbformat
from nbformat.v4 import new_code_cell, new_notebook

def py_to_ipynb(py_file, ipynb_file):
    with open(py_file, 'r') as f:
        py_code = f.read()

    # Create a new notebook
    nb = new_notebook()

    # Add code cells to the notebook from the Python file
    code_cells = py_code.split('\n\n')
    for cell_source in code_cells:
        nb.cells.append(new_code_cell(cell_source))

    # Write the notebook to the ipynb file
    with open(ipynb_file, 'w') as f:
        nbformat.write(nb, f)

def py_folder_to_ipynb(py_folder, ipynb_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(ipynb_folder):
        os.makedirs(ipynb_folder)

    # Loop through all .py files in the folder
    for py_file in os.listdir(py_folder):
        if py_file.endswith(".py"):
            # Form the full paths for input and output files
            py_file_path = os.path.join(py_folder, py_file)
            ipynb_file_path = os.path.join(ipynb_folder, py_file.replace(".py", ".ipynb"))

            # Convert .py file to .ipynb file
            py_to_ipynb(py_file_path, ipynb_file_path)

if __name__ == "__main__":
    py_folder = "PY_FOLDER_PATH"
    ipynb_folder = "DESTINATION_FOLDER_PATH"
    py_folder_to_ipynb(py_folder, ipynb_folder)
