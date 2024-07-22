import googlemaps.directions
import googlemaps.geolocation
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import googlemaps

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)


rate = engine.getProperty('rate')
engine.setProperty('rate', rate - 50)  # Adjust this value to set the speed to medium

aiName = 'Evelyn'
check = True

def talk(text):
    engine.say(text)
    engine.runAndWait()
    
talk('Hello, my name is '+ aiName +'  and I would like to help you today.')
def take_command():  
    try:
        with sr.Microphone() as source:
            
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if aiName in command:
                command = command.replace(aiName, '') 
                print(command)
    except:
        command = ""
    return command

def run_the_AI():
    global check
    command = take_command()
    print(command)
    if 'play' in command:
        response = command.replace('play', '')
        talk('playing' + response)
        pywhatkit.playonyt(response)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('The time is ' + time)
    elif 'who iseee' in command:
        search = command.replace('who is', '')
        info = wikipedia.summary(search, 1)
        print(info)
        talk(info)
    elif 'hey Evelyn':
        search = command.replace('Evelyn','')
        gmaps = googlemaps.Client(key='YOUR_API_KEY')
        getInfo = googlemaps.geolocation('https://www.google.com/maps/evelyn/live-more/real-time-traffic-update/ai/voice-activation/route-planning/navigation/current-conditions')
        talk()
    elif 'exit' in command:
        check = False
        print('Goodbye')
        talk('Thank you for chatting with me and i really love assisting you anytime. Goodbye')
    
    else:
        talk('Please repeat the command!')

while check: 
    run_the_AI()
