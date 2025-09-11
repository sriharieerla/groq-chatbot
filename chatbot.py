import os
from openai import OpenAI
from dotenv import load_dotenv
import speech_recognition as sr
import pyttsx3

# Load API key
load_dotenv()
client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

# Setup TTS engine
engine = pyttsx3.init()
engine.setProperty("rate", 170)   # speech speed
engine.setProperty("volume", 1.0) # max volume

# Setup Speech recognizer
recognizer = sr.Recognizer()
mic = sr.Microphone()

print("🎤 Voice Assistant Ready (say 'exit' to quit)\n")

while True:
    try:
        print("\nChoose input method: [1] Speak [2] Type")
        mode = input("Enter 1 or 2: ").strip()

        if mode == "1":  # Voice input
            with mic as source:
                recognizer.adjust_for_ambient_noise(source)
                print("Listening...")
                audio = recognizer.listen(source)

            try:
                user_input = recognizer.recognize_google(audio)
                print("You (voice):", user_input)
            except sr.UnknownValueError:
                print("⚠️ Could not understand audio. Try again.")
                continue
            except sr.RequestError as e:
                print(f"⚠️ Speech recognition error: {e}")
                continue

        else:  # Text input
            user_input = input("You (type): ")

        if user_input.lower() == "exit":
            print("Assistant: Goodbye! 👋")
            engine.say("Goodbye! See you soon.")
            engine.runAndWait()
            break

        # ✅ Groq API call with supported model
        response = client.chat.completions.create(
            model="qwen/qwen3-32b",  # stable model
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_input}
            ]
        )

        bot_reply = response.choices[0].message.content
        print("Assistant:", bot_reply)

        # Speak the reply
        engine.say(bot_reply)
        engine.runAndWait()

    except KeyboardInterrupt:
        print("\nAssistant: Goodbye! 👋")
        break
