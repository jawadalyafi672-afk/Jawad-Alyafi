import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

import time

import cohere
import pyttsx3

from dotenv import load_dotenv
from RealtimeSTT import AudioToTextRecorder


def speak(text):
    """Create a fresh TTS engine each time — reuse breaks after the first speak on Windows."""
    tts = pyttsx3.init()
    tts.setProperty("rate", 180)
    tts.say(text)
    tts.runAndWait()
    tts.stop()


def main():
    load_dotenv()

    # Cohere Client
    co = cohere.Client(
        os.getenv("COHERE_API_KEY")
    )

    # STT Recorder
    recorder = AudioToTextRecorder(
        post_speech_silence_duration=0.6,
    )

    print("Voice Assistant Started...")
    print("Speak now...")

    while True:

        # Speech -> Text
        user_text = recorder.text()

        if not user_text or not user_text.strip():
            continue

        print(f"\nUser: {user_text}")

        # Mute mic so speaker audio is not treated as a new question
        recorder.set_microphone(False)
        recorder.clear_audio_queue()

        # Text -> LLM (short answers work better for voice)
        response = co.chat(
            message=user_text,
            preamble=(
                "You are a helpful voice assistant. "
                "Keep answers short and clear, usually 1-3 sentences."
            ),
        )

        bot_reply = response.text

        print(f"Assistant: {bot_reply}")

        # Text -> Speech
        speak(bot_reply)

        # Clear leftover audio, then listen again
        time.sleep(0.4)
        recorder.clear_audio_queue()
        recorder.set_microphone(True)

        print("Speak now...")


if __name__ == "__main__":
    main()
