import os
import Anthropic

client = anthropic.Anthropic()
model=os.environ.get("LLM_MODEL", "claude-sonnet-5")
response = client.messages.create(
    model=model,
    max_tokens=256,
    messages=[{"role": "user", "content": "What is a neural network in one sentence?"}]
)
print(response.content[0].text)