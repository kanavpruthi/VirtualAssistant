import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia as wiki
import random
import pyjokes as jk
listener = sr.Recognizer()
engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
def talk(text='Retinal scan confirmed, welcome Agent Johnson, I am Jarvis.'):
    print(text)
    engine.say(text)
    engine.runAndWait()

talk()

def input_command():
    try:
        with sr.Microphone() as source:

            listener.adjust_for_ambient_noise(source)
            talk('Listening ...')
            voice=listener.listen(source)
            print('Kuch toh hua hai')
            command=listener.recognize_google(voice)
            command=command.lower()
            print(command)
            return command
    except:
        return "invalid"
        pass

def run_AI():
    command=input_command()
    while command=="invalid":
        talk("Sorry, didn't catch that. Please speak again")
        command=input_command()
    if 'play' in command:
        command=command.replace('jarvis','')
        song=command.replace('play','')
        talk('Playing '+song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time=datetime.datetime.now().strftime('%H:%M %p')
        talk('Currently, the time is '+time)
    elif 'what' in command or 'who' in command or 'where' in command:
        obj=command.replace('what','')
        obj=obj.replace('where','')
        obj=obj.replace('who','')
        info=wiki.summary(obj,2)
        talk(info)
    elif 'date' in command:
        ls=['Sorry love, I have a headache.',
        'I am flattered, but lets keep this professional, sir',
        'I think you are attractive, but I am not romantically interested in humans.']
        talk(ls[int(random.random()*len(ls))])
    elif 'are you single' in command:
        ls=['Name one married superhero.',
        'Just so you know, I choose fries over guys.',
         'I have a secret crush on Siri, but shush, don\'t tell anyone',
         'Two can play that game, you know.',
         'Yes, and that’s because I don’t want to burst my happy, lazy bubble.']
        talk(ls[int(random.random()*len(ls))])
    elif 'bored' in command or 'joke' in command or 'jokes' in command or 'boring' in command:
        talk(jk.get_joke())
    else:
        talk('I am currently learning new things, please go easy on me')

while True:
    run_AI()