import webbrowser
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia as wiki
import random
import pyjokes as jk
import subprocess as sb
import os


listener = sr.Recognizer()
engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)


def talk(text='Retinal scan confirmed, welcome Agent Johnson, I am Jarvis.'):
    print(text)
    engine.say(text)
    engine.runAndWait()

talk()

def opensite(site):
    webbrowser.open('http://www.'+site+'.com', new=2)

def openapp(command):
    if 'calculator' in command:
            sb.Popen('C:\\Windows\\System32\\calc.exe')
    elif 'notepad' in command:
        talk('Opening Notepad')
        os.system("Notepad")
    elif 'wordpad' in command:
        talk('Opening Wordpad')
        sb.Popen('C:\\Windows\\System32\\write.exe')
    elif 'google' in command or 'chrome' in command or 'browser' in command:
        talk('Opening Google Chrome')
        os.system('chrome')
    elif ("vlcplayer" in command) or ("player" in command) or ("video player" in command) or ("5" in command):
        talk('Opening VLC Media Player')
        os.system("VLC")
    elif ("illustrator" in command) or ("ai" in command) :
        talk('Opening Adobe Illustrator')
        os.system("illustrator")
    elif ("photoshop" in command) or ("ps" in command):
        talk('Opening Adobe Photoshop')
        os.system("photoshop")
    elif ("TELEGRAM" in command) or ("TG" in command) or ("10" in command):
        talk('Opening Telegram')
        os.system("telegram")
    elif ("excel" in command) or ("msexcel" in command) or ("sheet" in command):
        talk('Opening MS Excel')
        os.system("excel")
    elif ("slide" in command) or ("mspowerpoint" in command) or ("ppt" in command) or ("powerpnt" in command) :
        talk('Opening Ms Powerpoint')
        os.system("powerpnt")
    elif ("word" in command) or ("msword" in command):
        talk('Opening MS Word')
        os.system("winword")

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

x=True

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
    elif 'open' in command:
        openapp(command)
        if 'youtube' in command:
            opensite('youtube')
        elif 'facebook' in command:
            opensite('facebook')
        elif 'instagram' in command:
            opensite('instagram')
        elif 'github' in command or 'git' in command or 'repository' in command:
            opensite('github')
        elif 'amazon'in command:
            opensite('amazon')
        elif 'flipkart' in command:
            opensite('flipkart')
        elif 'snapdeal' in command:
            opensite('snapdeal')
        elif 'gmail' in command:
            opensite('gmail')
    elif 'stop' in command or 'exit' in command:
        talk('Shutting Jarvis down.')
        talk('Sorry to see that you are leaving.')
        return False
    else:
        talk('I am currently learning new things, please go easy on me')
    return True

while x:
    x=run_AI()