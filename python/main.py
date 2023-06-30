import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import requests

listner = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.say("I am your Shakil")
engine.say("What can I do for you")
engine.runAndWait()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def talk_command():
    try:
        with sr.Microphone() as source:
            listner.adjust_for_ambient_noise(source)
            print('listening...')
            voice = listner.listen(source)
            print(voice)
            command = listner.recognize_google(voice)
            command = command.lower()
            print(command)
            # if 'alexa' in command:
            #     command = command.replace('alexa', '')
            #     talk(command)
    except:
        pass
    return command

# def talk_command_fromdate():
#     try:
#         with sr.Microphone() as fromdate:
#             print('listening...')
#             voicefromdate = listner.listen(fromdate)
#             commandfromdate = listner.recognize_google(voicefromdate)
#             commandfromdate = commandfromdate.lower()
#     except:
#         pass
#     return commandfromdate

# def tald_command_todate():
#     try:
#         with sr.Microphone() as todate:
#             print('todate listening...')
#             voicetodate=listner.listen(todate)
#             commandtodate=listner.recognize


def run_alexa():
    command = talk_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)  # For opening youtube
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is '+time)
    elif 'who the heck is' in command:
        person = command.replace('who the heck is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry, I have a headache')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'joke' in command:
        joke = pyjokes.get_joke()
        print(joke)
        talk(joke)
    elif 'schedule' in command:
        # commandfromdate=commandfromdate()
        query = {
            "email": "bony2669@gmail.com",
            "fromDate": "2022-11-10",
            "toDate": "2023-12-10"
        }
        response = requests.post(
            "http://192.46.212.177:3008/api/alexa/schedule", data=query)
        responseJsonData = response.json()
        print(responseJsonData['details'])
        talk('Your '+responseJsonData['details']['child_or_parent'] +
             ' name is '+responseJsonData['details']['name']+'. Your schedules are')
        for x in responseJsonData['details']['child_details']:
            talk('Your schedule held on ' + x['date'].replace('T00:00:00.000Z','') + ' at '+x['start_time'].replace('T00:00:00.000Z','') + ' to ' + x['end_time'] +
                 '. This schedule name is ' + x['schedule_name'] + ' play with the sport ' + x['sport_name'])
        # response = requests.get("http://api.open-notify.org/astros.json")
        # for x in responseJsonData['people']:
        #     print(x)
        #     talk('Name is '+x['name'] + ' and craft is '+x['craft'])

    else:
        talk('Please say the command again')


while True:
    run_alexa()
