# Huggingface
def load_huggingface_model(model_id="bert-base-uncased"):
    print(f"Loaded HF model: {model_id}")
    return lambda prompt: f"HF {model_id} response to: {prompt}"
