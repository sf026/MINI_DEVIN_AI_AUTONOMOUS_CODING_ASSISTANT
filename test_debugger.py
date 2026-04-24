from agents.debugger import fix_code

# Intentionally wrong code
code = "print(Hello)"

error = "NameError: name 'Hello' is not defined"

fixed = fix_code(code, error)

print(fixed)