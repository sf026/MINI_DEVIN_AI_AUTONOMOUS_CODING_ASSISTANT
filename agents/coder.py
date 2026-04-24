from core.llm import ask_llm


def generate_code(task):
    prompt = f"""
You are an expert Python developer. Generate a multi-file Python project.

YOU MUST FOLLOW THIS EXACT OUTPUT FORMAT — NO EXCEPTIONS:

FILE: utils.py
(put ALL helper functions, classes, logic here)

FILE: app.py
(put ONLY the main() function here, import from utils)

CRITICAL RULES:
- Output EXACTLY two files: utils.py and app.py
- utils.py must contain ALL functions except main()
- app.py must ONLY contain the main() function and imports
- app.py must import from utils using: import utils OR from utils import ...
- NO markdown, NO backticks, NO explanations, NO comments in English
- Proper 4-space indentation on every line inside functions/classes
- Do NOT use input() — use hardcoded test values instead
- Code must be 100% runnable with no errors

EXAMPLE FORMAT (follow this structure exactly):

FILE: utils.py
def greet(name):
    return f"Hello, {{name}}!"

FILE: app.py
from utils import greet

def main():
    print(greet("Alice"))

if __name__ == "__main__":
    main()

Now generate code for this task:
{task}
"""
    return ask_llm(prompt)


def generate_simple_code(task):
    prompt = f"""
Write a complete, working Python program in ONE file.

RULES:
- Single file only
- All functions must be defined BEFORE they are called
- No explanations, no markdown, no backticks
- Proper 4-space indentation
- Must run without any errors
- Do NOT use input() — use hardcoded test values

Task:
{task}
"""
    return ask_llm(prompt)