# Llm
def load_llm_model(model_name="openai"):
    print(f"Loaded LLM model: {model_name}")
    return lambda prompt: f"{model_name} response to: {prompt}"
