import speech_recognition as sr
import datetime
import pyttsx3
import calendar

# Initialize the recognizer
r = sr.Recognizer()

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Find a female voice by iterating over the available voices and checking the gender attribute
female_voice = None
voices = engine.getProperty('voices')
for voice in voices:
    if voice.gender == 'female':
        female_voice = voice
        break

# Set the engine's voice to the female voice
if female_voice:
    engine.setProperty('voice', female_voice.id)

# Set the speaking rate to a comfortable level
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-20)

# Define the speak function to speak the given text using the engine
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Define the time function to speak the current time using the engine
def time():
    now = datetime.datetime.now()
    speak("The time is " + now.strftime("%H:%M"))

# Define the date function to speak the current date using the engine
def date():
    now = datetime.datetime.now()
    day = str(now.day)
    month_name = calendar.month_name[now.month]
    year = str(now.year)
    speak("Today is " + day + " " + month_name + " " + year)

# Define the activate_function to initiate the conversation
def activate_function():
    speak("Hello, how can I help you?")

# Define the main loop that listens for voice input and performs actions based on the recognized text
while True:
    # Use the microphone as a source
    with sr.Microphone() as source:
        print("Please speak, I am listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    # Convert speech to text
    try:
        text = r.recognize_google(audio)
        print("You said:", text)
        if "alexa" in text.lower():
            activate_function()
        if "time" in text.lower():
            time()
        if "date" in text.lower():
            date()
        if "power off" in text.lower() or "turn off" in text.lower() or "stop" in text.lower():
            speak("Goodbye!")
            break  # exit the loop if "stop" is said

    except sr.UnknownValueError:
        print("Sorry, I could not understand your speech")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    except Exception as e:
        print("Error:", e)
