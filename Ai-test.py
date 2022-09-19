import os
import openai

# Load your API key from an environment variable or secret management service
openai.api_key = "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"

response = openai.Completion.create(model="text-davinci-002", prompt="Say this is a test", temperature=0, max_tokens=6)