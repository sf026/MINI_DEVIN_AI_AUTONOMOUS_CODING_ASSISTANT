import subprocess
import os


def run_code(file_path):
    current_dir = os.getcwd().replace("\\", "/")

    command = (
        f'docker run --rm -v "{current_dir}":/app -w /app/output '
        f'python:3.10 python app.py'
    )

    result = subprocess.run(command, shell=True, capture_output=True, text=True)

    return result.stdout, result.stderr