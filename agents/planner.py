from core.llm import ask_llm

def plan_task(user_input):
    prompt = f"""
    You are a planner agent.

    Break the task into SHORT and CLEAR steps.

    Rules:
    - Only give 4 to 6 steps
    - Each step must be one line
    - No explanation
    - No code

    Task:
    {user_input}
    """

    return ask_llm(prompt)