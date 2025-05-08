import os

# Root directory of the package
root_dir = "agentplanner"
os.makedirs(root_dir, exist_ok=True)

# Subdirectories and files to create
structure = {
    "agentplanner": [
        "__init__.py",        # Initialization file
        "core.py",            # Core functionalities of AgentPlanner
        "llm.py",             # LLM interaction logic
        "chains.py",          # Chains like SimpleChain, SequentialChain, ParallelChain
        "embedding.py",       # Embedding functionalities
        "huggingface.py",     # Hugging Face specific code
        "cloud.py",           # Cloud connections (AWS, Azure, GCP, etc.)
        "orchestration.py",   # Orchestrating the execution flow
        "docker.py"           # Docker setup or .docker methods
    ],
    "examples": [
        "use_agentplanner.py"  # Example usage of the framework
    ],
}

# Create directories and empty files
for folder, files in structure.items():
    folder_path = os.path.join(root_dir, folder)
    os.makedirs(folder_path, exist_ok=True)
    
    # Create files within the folders
    for file in files:
        file_path = os.path.join(folder_path, file)
        with open(file_path, "w") as f:
            f.write("# " + file.replace(".py", "").capitalize() + "\n")  # Placeholder content