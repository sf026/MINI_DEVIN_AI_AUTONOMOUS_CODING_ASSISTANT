from core.llm import ask_llm


def fix_code(code, error):
    prompt = f"""TASK: Fix broken Python code.

ERROR:
{error}

BROKEN CODE:
{code}

OUTPUT FORMAT — start your response with "FILE: utils.py" immediately, nothing before it:

FILE: utils.py
<fixed utils code here>

FILE: app.py
<fixed app code here>

STRICT RULES:
- Your response MUST start with "FILE: utils.py" — no other text before it
- NO sentences like "Here are the corrected files" or "I fixed the code"
- NO markdown, NO backticks, NO explanations whatsoever
- Fix the specific error: {error}
- If error is "missing argument", fix the function CALL to pass all required arguments
- If error is "module has no attribute", move the function to utils.py
- Proper 4-space indentation
- Do NOT use input()
- app.py must import from utils"""
    return ask_llm(prompt)