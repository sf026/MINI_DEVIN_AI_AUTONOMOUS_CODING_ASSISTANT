from tools.file_manager import save_file

code = "print('Hello from AI')"

result = save_file("output/app.py", code)

print(result)