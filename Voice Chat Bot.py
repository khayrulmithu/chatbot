# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 11:32:11 2023

1. Speech Recognition
2. Text to speech
3. py audio

this take so much time : pip install playsound==1.2.2
latest version not working

@author: KHAYRUL
"""


import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
import wikipedia
import pyjokes

import os

from playsound import playsound

from gtts import gTTS

if os.path.exists('hello.mp3'):
    os.remove('hello.mp3')


listener = sr.Recognizer()
robot = pyttsx3.init()

voices = robot.getProperty('voices')
robot.setProperty('voice', voices[1].id)
robot.setProperty('rate', 100)

text = "হাই আমি রোবট  ক্রিস্টিনা ,  আমি আপনাকে কিভাবে সাহায্য করতে পারি স্যার "

# if os.path.exists('hello.mp3'):
#     os.remove('hello.mp3')
    
# if os.path.exists('nidhi.mp3'):
#     playsound('nidhi.mp3',True)
    
def talk(text):
    robot.say(text)
    robot.runAndWait()
    


def bangla_voice(text):
    tts = gTTS( text ,  lang='bn')
    tts.save('hello.mp3')
 
def bangla_play():
    if os.path.exists('hello.mp3'):
        playsound('hello.mp3')
        
        os.remove('hello.mp3')
    
bangla_voice(text)
bangla_play()
shutdown = 0
night=0
morning=0
noon=0

def take_command():
    
    try:
        
        with sr.Microphone() as source:
            
            print('Listening......')
            
            listener.adjust_for_ambient_noise(source)
            
            voice = listener.listen(source,5,10)
            
            command = listener.recognize_google(voice, language='eng-bn')
            
            command_bangla = listener.recognize_google(voice, language='bn')
            
            command = command.lower();
            
            print(command)
            #talk(command)
            
            print(command_bangla)
            
            if 'christina' in command or 'kristina' in command:
                command = command.replace('christina','')
                command = command.replace('kristina','')
                
            else:
                command=command
                #bangla_voice(text)
        
        
    except:
        command = "Hi"
    
    return command

def run_robot():
    command = take_command()
    
    if 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is' + time)
        
    elif  "সময়"  in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        bangla_voice('এখন সময় হচ্ছে' )
        bangla_play()
        talk(time)
        
    elif 'play' in command: 
        song = command.replace('play','')
        talk('playing  ' + song)
        pywhatkit.playonyt(song)
        
    elif 'joke' in command:
        joke=pyjokes.get_jokes(language='en')
        print(joke)
        talk(joke)
        
    elif 'tell me about' in command or 'what is' in command:
        look_for = command.replace('tell me about', '')
        look_for = command.replace('what is', '')
        print('Looking for :' + look_for)
        info = wikipedia.summary(look_for, 2)
        print(info)
        talk(info)
                
        
    elif 'i love you' in command:
        talk('I love you too shona')
        
    elif 'shut down' in command:
        global shutdown
        shutdown = 1
        
    elif 'search' in command:
        pywhatkit.search(command)
        print(command)


while True:
    
    time = datetime.datetime.now().strftime('%H')
    
    
    
    if time=='10' and morning == 0 :
        bangla_voice('জান সকালে খাইছো')
        bangla_play()
        mornige=1
        
        
    elif time=='13' and noon == 0 :
        bangla_voice('জান  দুপুরে খাইছো')
        bangla_play()
        noon=1
    
    elif time=='22' or time=='23' and night == 0 :
        bangla_voice('জান রাতে খাইছো')
        bangla_play()
        night=1
    
    if shutdown==1:
        talk('Yes shona. I am shutdown myself')
        break
    
    run_robot()