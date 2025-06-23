"""
llm.py: Wrapper for OpenAI ChatCompletion API.
"""
import os
import openai

# Make sure to set OPENAI_API_KEY in your environment
openai.api_key = os.getenv("OPENAI_API_KEY")


def ask(messages: list[dict]) -> str:
    """
    Sends a chat completion request and returns assistant's reply.
    messages: list of {'role': 'system'|'user'|'assistant', 'content': str}
    """
    # Use new OpenAI Python v1.x API
    response = openai.chat.completions.create(
        model="gpt-4o",
        messages=messages
    )
    return response.choices[0].message.content.strip()
