# Voice AI Assistant

Listens to your voice, replies with Cohere, then speaks the answer.

**Flow:** Speech → Text → Cohere → Speech

## Requirements

- Windows + Python 3.10+
- Microphone and speakers
- Cohere API key

## Setup

1. Open the project folder:

```bat
cd Desktop\voice-ai-assistant
```

2. Install packages:

```bat
python -m pip install cohere python-dotenv pyttsx3 "RealtimeSTT[faster-whisper]"
```

On Python 3.13+, also run:

```bat
python -m pip install audioop-lts
```

3. Create a `.env` file:

```env
COHERE_API_KEY=your_api_key_here
```

4. Run:

```bat
python AiVoice.py
```

Speak when you see `Speak now...`. Press `Ctrl + C` to stop.

## Notes

- First run may download the Whisper model.
- `realtimesst.log` is optional debug output and can be deleted.
