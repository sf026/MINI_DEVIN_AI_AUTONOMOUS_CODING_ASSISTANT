# 🚀 Mini Devin — AI Autonomous Coding Assistant

Mini Devin is an **Agentic AI system** that can **plan, generate, debug, and execute Python code autonomously** from a simple natural language instruction.

Inspired by Devin AI, this project demonstrates how multi-agent systems can simulate a real-world software development workflow — **completely free and running locally**.

---

##  What is Mini Devin?

Mini Devin is not just a chatbot.

It is an **autonomous AI coding agent** that:

- Understands user requirements in plain English  
- Breaks tasks into structured steps  
- Generates clean Python code  
- Executes the code automatically  
- Detects runtime errors  
- Fixes errors using an AI debugging loop  

 From idea → working code, without manual coding.

---

##  How It Works

The system follows an **Agentic AI workflow**:
- User Input → Planner Agent → Coder Agent → Execution → Debug Agent → Final Output

  
### 🔹 Step-by-Step Flow

1. **User Input**  
   User provides a task (e.g., “Create a calculator app”)

2. **Planner Agent**  
   Breaks the task into structured steps

3. **Coder Agent**  
   Generates Python files (`app.py`, `utils.py`)

4. **Validation**  
   Cleans and validates code using `compile()`

5. **Execution**  
   Runs the generated code

6. **Debug Loop**  
   If errors occur:
   - Captures traceback  
   - Sends error + code to Debug Agent  
   - Fixes and retries (up to 3 times)

7. **Final Output**  
   Displays working result in UI

---

## 🤖 Multi-Agent Architecture

| Agent | Responsibility |
|------|----------------|
| Planner Agent | Task decomposition |
| Coder Agent | Code generation |
| Debug Agent | Error detection & fixing |

👉 Each agent has a **single responsibility**, similar to a real dev team.

---

##  Tech Stack

- Python 3.10+
- LangChain (Agent orchestration)
- Ollama (Local LLM runtime)
- Llama 3 (AI model)
- Streamlit (UI)
- Docker (optional sandbox execution)

---

---

## 🚀 Features

- 🤖 Multi-agent AI system  
- 🔁 Autonomous planning → coding → debugging loop  
- 🔧 Automatic error fixing (retry mechanism)  
- 🧹 Output cleaning and syntax validation  
- 📁 Multi-file project generation  
- 🌐 Interactive Streamlit UI  
- 💸 100% free (runs locally, no API keys)

---
### Limitations
- Limited to Python projects
- No memory across runs
- Small local model limitations
- Fixed number of output files
- Debugger uses same LLM (may be inconsistent)

### Future Enhancements
- Stronger coding models (CodeLlama / DeepSeek-Coder)
- Multi-language support (React, Node.js)
- Persistent memory
- GitHub integration
- Full Docker sandboxing
- Autonomous web browsing agent  

### Learning Outcomes
This project demonstrates:

- Agentic AI system design
- Multi-agent orchestration
- LLM prompt engineering
- Autonomous feedback loops
- AI-driven software development workflows

### ? Why This Project Matters

- **Most AI tools assist developers.**
- **Mini Devin goes further — it acts like a developer.**
