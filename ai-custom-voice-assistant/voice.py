"""
voice.py: Provides speech-to-text and text-to-speech using SpeechRecognition and pyttsx3.
"""
import os
import io
import speech_recognition as sr
import pyttsx3
from dotenv import load_dotenv
from openai import OpenAI
import openai
import tempfile

# Load environment and set OpenAI API key
load_dotenv()
# Instantiate v1 client (reads API key from env)
client = OpenAI()

# Initialize TTS engine
engine = pyttsx3.init()
# Capture default rate and define slow rate for spelling
default_rate = engine.getProperty('rate')  # e.g., ~200
slow_rate = int(default_rate * 0.5)         # 50% speed for spelling

def speak(text: str):
    """
    Convert text to speech.
    """
    engine.say(text)
    engine.runAndWait()

def speak_slow(text: str):
    """
    Speak text at a slower rate (useful for spelling out names/emails).
    """
    engine.setProperty('rate', slow_rate)
    engine.say(text)
    engine.runAndWait()
    engine.setProperty('rate', default_rate)

def listen(prompt: str = None) -> str:
    """
    Listen via microphone and return recognized text.
    """
    if prompt:
        speak(prompt)
    # Record audio from microphone
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        audio = recognizer.listen(source)
    try:
        # Convert to WAV bytes
        wav_bytes = audio.get_wav_data()
        # Write to a temporary file with .wav extension
        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmp:
            tmp.write(wav_bytes)
            tmp_path = tmp.name
        try:
            # Transcribe via Whisper using v1 client API
            with open(tmp_path, 'rb') as f:
                response = client.audio.transcriptions.create(
                    model="whisper-1",
                    file=f
                )
            text = response.text.strip()
        finally:
            try:
                os.unlink(tmp_path)
            except OSError:
                pass
        if not text:
            raise ValueError("Empty transcription result")
        return text
    except Exception as e:
        # Log the underlying error for debugging
        print(f"[STT Error] {type(e).__name__}: {e}")
        # Prompt user to retry
        speak("Sorry, I didn't catch that. Please repeat your response.")
        return listen(prompt)
