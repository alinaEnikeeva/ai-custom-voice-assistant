"""
main.py: Entry point for AI Assistant PoC with dynamic AI-driven dialogue.
"""
import os
from dotenv import load_dotenv
load_dotenv()
import logging
from ringcx import receive_call
from logger import setup_logging
from llm import ask
from voice import listen, speak, speak_slow


def is_spelling_prompt(text: str) -> bool:
    """
    Determine if the assistant is asking for spelling confirmation (slow speech).
    """
    text_lower = text.lower()
    return "spell" in text_lower or "spelling" in text_lower or text_lower.startswith("i have your name")


def main():
    setup_logging()
    logging.info("Starting AI-powered Call Assistant...")

    # Simulate incoming call
    call_id, _ = receive_call()

    # Initialize conversation with system prompt
    system_prompt = (
        "You are a voice-based call assistant. "
        "Greet the caller and ask 'How can I help you today?'. "
        "If the caller wants order status, ask for order number and name, then provide status. "
        "If the caller wants to order orthotic flip-flops, gather shoe size, delivery address, full name, and email, then confirm pricing and delivery. "
        "After collecting the full name and email, repeat them back to the caller and ask them to confirm the spelling before proceeding. "
        "If you cannot understand or classify the request, say you'll escalate to a human agent."
    )
    messages = [{"role": "system", "content": system_prompt}]

    # Assistant's first prompt
    assistant_msg = ask(messages)
    # Speak and display assistant prompt
    print(f"AI Assistant: {assistant_msg}")
    # Use slower TTS for spelling prompts
    if is_spelling_prompt(assistant_msg):
        speak_slow(assistant_msg)
    else:
        speak(assistant_msg)
    messages.append({"role": "assistant", "content": assistant_msg})

    # Conversation loop
    while True:
        # Listen for user response
        user_input = listen()
        print(f"Customer: {user_input}")
        if user_input.lower() in ["exit", "quit"]:
            farewell = "Thank you! Connecting you to a human agent now. Goodbye."
            print(f"AI Assistant: {farewell}")
            speak(farewell)
            break
        messages.append({"role": "user", "content": user_input})
        assistant_msg = ask(messages)
        print(f"AI Assistant: {assistant_msg}")
        # Slow down spelling confirmations
        if is_spelling_prompt(assistant_msg):
            speak_slow(assistant_msg)
        else:
            speak(assistant_msg)
        messages.append({"role": "assistant", "content": assistant_msg})


if __name__ == '__main__':
    # Ensure API key is set
    if not os.getenv("OPENAI_API_KEY"):
        print("Error: Please set the OPENAI_API_KEY environment variable.")
    else:
        main()
