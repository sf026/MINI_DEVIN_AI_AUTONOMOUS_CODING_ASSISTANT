from sandbox.runner import run_code

output, error = run_code("output/app.py")

print("OUTPUT:\n", output)
print("ERROR:\n", error)