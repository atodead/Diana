import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import smtplib
import requests, json
from twilio.rest import Client
listener = sr.Recognizer()
vroom = pyttsx3.init()
voices = vroom.getProperty('voices')
server = smtplib.SMTP('smtp.gmail.com', 587)
vroom.setProperty('voice', voices[1].id)


def talk(text):
    vroom.say(text)
    vroom.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            talk('listening...')
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'diana' in command:
                command = command.replace('diana', '')
                talk('You told:'+command)
                print(command)
    except:
        talk("sorry, i couldn't hear you. check your microphone and try again.")
    return command


def run_diana():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'tell me more about' in command:
        person = command.replace('who the is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'email' in command:
        email1 = str(input('Your email please:'))
        password = str(input('Your password please:'))
        recv = input('the person you want to send the email to:')
        content = str(input('The content of the message(Please write in one line only.):'))
        server.starttls()
        server.login(email1, password)
        server.sendmail(
            email1,
            recv,
            content
        )
    elif 'tell me a joke' in command:
        gimmejokes = pyjokes.get_joke()
        talk(gimmejokes)
        print(gimmejokes)
    elif 'who is your father' in command:
        talk('The best programmer on earth, the smartest kid on earth, Aneeketh Shait.')
    elif 'thank you' in command:
        talk('Anything for you!')
    elif 'good night' in command:
        talk("Goodnight, sweet dreams and Oh! I almost forgot, don't let the bedbugs bite!")
        print("Goodnight, sweet dreams and Oh! I almost forgot, don't let the bedbugs bite!")
    elif 'who is better you or siri' in command:
        talk('is that even a question? Of course it is me!')
    elif 'who is better you or alexa' in command:
        talk('is that even a question? Of course it is me!')
    elif 'calculate' in command:
        ask = str(input('the operation you want to conduct:'))
        a = int(input('the first number:'))
        b = int(input('the second number'))
        if 'addition' in ask:
            method = a + b
            talk(method)
            print('The answer is:', method)
        if 'subtraction' in ask:
            method = a - b
            talk(method)
            print('The answer is:', method)
            print('The answer is:', method)
        if 'multiplication' in ask:
            method = a * b
            talk(method)
            print('The answer is:', method)
        if 'division' in ask:
            method = a / b
            talk(method)
            print('The answer is:', method)
    elif 'weather' in command:
        base__url = "https://api.openweathermap.org/data/2.5/weather?"
        city = str(input('City you want to know the weather about(or nearest city also):'))
        api_key = ''#your api key
        URL = base__url + "q=" + city + "&appid=" + api_key
        response = requests.get(URL)
        if response.status_code == 200:
            data = response.json()
            main = data['main']
            temperature = main['temp']
            humidity = main['humidity']
            pressure = main['pressure']
            report = data['weather']
            talk(f"{city:-^30}")
            print(f"{city:-^30}")
            talk(f"Temperature: {temperature}")
            print(f"Temperature: {temperature}")
            talk(f"Humidity: {humidity}")
            print(f"Humidity: {humidity}")
            talk(f"Pressure: {pressure}")
            print(f"Pressure: {pressure}")
            talk(f"Weather Report: {report[0]['description']}")
            print(f"Weather Report: {report[0]['description']}")
        else:
            print("Error in the HTTP request")
    elif 'tell me what you can do' in command:
        talk('i can do many things. I can tell you a joke, send an email, play songs, and tell you who is my father, and i will also tell you the weather to the nearest city if you wanted to!')
        print('i can do many things. I can tell you a joke, send an email, play songs, and tell you who is my father, and i will also tell you the weather to the nearest city if you wanted to!')

    elif "i don't know what i should do" in command:
        talk('Go do what you like to have fun!')

    elif 'tell me about yourself' in command:
        talk("I am Diana, master Aneeketh's smart voice assistant. I'm named after princess diana from the amazons, inspired by the amazons of greek mythology. And, i love my name!")

    elif 'call' in command:
        rec = str(input('Person you want to call(with country code):'))
        account_sid = '' #put in your acc sid
        auth_token = ''#put in your acc authtoken
        client = Client(account_sid, auth_token)
        call = client.calls.create(twiml='<Response><Say>Hello this is call is made by diana</Say></Response>', to=rec, from_='')#put your twilio phone number in from_

        print(call.sid)
    else:
        talk('please say the command again.')
while True:
    run_diana()
