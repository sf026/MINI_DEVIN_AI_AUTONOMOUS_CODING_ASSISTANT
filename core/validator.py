def is_valid_python(code):
    try:
        compile(code, "<string>", "exec")
        return True
    except Exception as e:
        return False