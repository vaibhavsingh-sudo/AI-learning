import os
import json
import urllib.request

from sympy import content

url ="https://api.anthropic.com/v1/messages"
headers = {
    "Content-Type": "application/json",
    "x-api-key": os.environ.get("ANTHROPIC_API_KEY")
}
body =json.dumps({
    "model":os.environ.get("LLM_MODEL","claude-sonnet-5"),
    "max_tokens":256,
    "messages":[{"role":"user","content":"What is a neural network in one sentence?"}],
}).encode()
req=urllib.request.Request(url,data=body,headers=headers, method="POST")
with urllib.request.urlopen(req) as resp:
    result=json.loads(resp.read())
    print(result["content"][0]["text"])
