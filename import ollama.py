# Use a pipeline as a high-level helper
from transformers import pipeline

pipe = pipeline("text-generation", model="Akicou/GLM-4.7-Flash-REAP-50")
messages = [
    {"role": "user", "content": "Who are you?"},
]
pipe(messages)