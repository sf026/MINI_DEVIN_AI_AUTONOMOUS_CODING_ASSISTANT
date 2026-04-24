from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="llama3")

def ask_llm(prompt):
    return llm.invoke(prompt)