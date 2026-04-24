def parse_files(response):
    files = {}
    current_file = None

    for line in response.split("\n"):
        stripped = line.strip()

        # Detect FILE: marker
        if stripped.startswith("FILE:"):
            current_file = stripped.replace("FILE:", "").strip()
            files[current_file] = []
            continue

        # Detect **filename.py** marker
        elif stripped.startswith("**") and stripped.endswith("**"):
            current_file = stripped.replace("*", "").strip()
            files[current_file] = []
            continue

        # Add content using ORIGINAL line (preserve indentation)
        if current_file:
            files[current_file].append(line)

    # Join content lines
    for file in files:
        files[file] = "\n".join(files[file])

    return files  