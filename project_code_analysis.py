import os
import subprocess

def run_pylint(file_path):
    try:
        result = subprocess.run(['pylint', file_path], capture_output=True, text=True)
        print(f"Pylint analysis for {file_path}:")
        print(result.stdout)
    except Exception as e:
        print(f"Error running Pylint: {e}")

def run_pep8(file_path):
    try:
        result = subprocess.run(['pycodestyle', file_path], capture_output=True, text=True)
        print(f"PEP8 analysis for {file_path}:")
        print(result.stdout)
    except Exception as e:
        print(f"Error running PEP8: {e}")

def check_incomplete_code(file_path):
    incomplete_keywords = ['TODO', 'FIXME', 'TBD']
    with open(file_path, 'r') as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            for keyword in incomplete_keywords:
                if keyword in line:
                    print(f"Incomplete code found in {file_path} at line {i+1}: {line.strip()}")

if __name__ == "__main__":
    project_dir = "./workspace/sudoku_game_01/sudoku_game"  # Replace with the path to your generated project
    for root, dirs, files in os.walk(project_dir):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                run_pylint(file_path)
                run_pep8(file_path)
                check_incomplete_code(file_path)
