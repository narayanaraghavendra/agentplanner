# AgentPlanner

AgentPlanner is a simple, modular framework for LLM operations, embeddings, Hugging Face integration, cloud services, and orchestration—without LangChain.

## Features

- Run OpenAI or HF models
- Generate embeddings
- Chain prompts (Simple, Sequential, Parallel)
- Orchestrate cloud services (AWS, GCP, Azure, etc.)
- All in one class: `AgentPlanner`

## Example

```python
from agentplanner import AgentPlanner

agent = AgentPlanner()
response = agent.run("Translate this to French.", steps=["llm:openai", "embedding"])
print(response)



