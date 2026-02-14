import speech_recognition as sr
import pyttsx3
import random
import time

engine = pyttsx3.init()

# Select voice (0 = male, 1 = female)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# Speed + volume
engine.setProperty('rate',150)
engine.setProperty('volume',1.0)

def speak(text):
    print("AI:", text)
    engine.stop()
    engine.say(text)
    engine.runAndWait()

questions = [
    # PART 1 – Introduction
    "Let us begin. Can you tell me about yourself?",
    "Where are you from?",
    "Are you a student or do you work?",
    "Why did you choose your field of study?",
    "What do you usually do in your free time?",

    # PART 1 – Daily life
    "Do you enjoy listening to music?",
    "What kind of movies do you like?",
    "Do you prefer mornings or evenings?",
    "How often do you use the internet?",

    # PART 2 – Cue card style
    "Now I would like you to describe a memorable day in your life. You should say when it was, what happened, and why it was memorable.",
    "Describe a person who has influenced you. You should say who the person is, how you know them, and why they are important to you.",
    "Describe your hometown. You should say where it is, what it is like, and what you like about it.",

    # PART 3 – Discussion
    "Why do you think people like to travel?",
    "How has technology changed the way people communicate?",
    "Do you think education is important for success?",
    "What are the advantages of living in a big city?",
    "Should young people focus more on career or family?"
]

r = sr.Recognizer()

speak("Welcome to IELTS speaking practice.")

while True:

    q = random.choice(questions)
    speak(q)

    # pause after question
    time.sleep(1)

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=0.5)
        print("Speak...")
        audio = r.listen(source)

    try:
        user = r.recognize_google(audio)
        print("You:", user)

        if user.lower() == "stop":
            speak("Practice finished.")
            break

        speak("Thank you. Next question.")

        # pause before next question
        time.sleep(1)

    except:
        speak("Say again.")
