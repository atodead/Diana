import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import smtplib
listener = sr.Recognizer()
vroom = pyttsx3.init()
voices = vroom.getProperty('voices')
server = smtplib.SMTP('smtp.gmail.com', 587)


def talk(text):
    vroom.say(text)
    vroom.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'edith' in command:
                command = command.replace('edith', '')
                print(command)
    except:
        pass
    return command


def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who the heck is' in command:
        person = command.replace('who the is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'email' in command:
        email1 = str(input('Your email please:'))
        password = str(input('Your password please'))
        recv = input('the person you want to send the email to:')
        content = str(input('The content of the message(Please write in one line only.):'))
        server.starttls()
        server.login(email1, password)
        server.sendmail(
            email1,
            recv,
            content
        )
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('Please say the command again.')


while True:
    run_alexa()
