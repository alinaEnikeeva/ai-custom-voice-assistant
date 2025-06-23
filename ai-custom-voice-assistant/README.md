# AI Assistant PoC

This proof-of-concept simulates a production-grade AI assistant pipeline:

- Ingests live calls via RingCX stub
- Converts audio to text via stubbed STT
- Performs intent detection
- Fetches order data from NetSuite stub
- Routes calls or escalates to human agent
- Logs activity with timestamps

## Directory Structure

```text
ai_assistant_poc/
├── main.py          # Entry point running AI-driven dialogue
├── ringcx.py        # Stub for RingCX call ingestion
├── llm.py           # Wrapper for OpenAI ChatCompletion API
├── voice.py         # Speech-to-text and text-to-speech I/O
├── logger.py        # Logging configuration
├── README.md        # This instructions file
└── tests/           # (Optional) add unit tests here
```

## Requirements

- Python 3.8+
- OpenAI Python client
- python-dotenv
- SpeechRecognition
- pyttsx3

## Setup & Run

1. (Optional) Create and activate a virtual environment:

   ```zsh
   python3 -m venv venv
   source venv/bin/activate
   ```

2. Install dependencies via requirements file:

   ```zsh
   pip install -r requirements.txt
   ```

   # If you run into audio backend errors, install system libraries:

   # On macOS:

   brew install portaudio
   pip install PyAudio

   # On Linux:

   sudo apt-get install portaudio19-dev python3-pyaudio

3. Configure environment:

   ```zsh
   # Create a `.env` file in this directory with:
   # OPENAI_API_KEY=your_api_key_here
   echo 'OPENAI_API_KEY=your_api_key_here' > .env
   ```

4. Run the PoC:

   ```zsh
   python main.py
   ```

5. To exit the conversation:
   - Say or type `exit` or `quit`

## Next Steps

- Implement real RingCX, NetSuite integrations.
- Add persistent state or databases for orders.
- Add error handling, retries, metrics, and monitoring.
