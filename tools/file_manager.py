import os

def save_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

    return f"File saved at {path}"