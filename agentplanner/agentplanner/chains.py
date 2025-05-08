# Chains
def simple_chain(prompt, model):
    return model(prompt)

def sequential_chain(prompts, model):
    result = ""
    for i in prompts:
        result = model(f"{result} {i}")
    return result

def parallel_chain(prompts, model):
    return [model(i) for i in prompts]
