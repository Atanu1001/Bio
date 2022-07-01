import speech_recognition as s_r
import pyttsx3
import subprocess
import webbrowser
import datetime
import wikipedia
import winshell
import time
import yagmail
import pyjokes
import bs4
import requests
import os
# my own program
import Calender
import player



#functions
def audio_input(): # takes the audio as input from the user and converts into a string
    rec = s_r.Recognizer()
    my_mike = s_r.Microphone()
    print(f"{botname}: listening......\n")

    with my_mike as source:
        rec.adjust_for_ambient_noise(source)
        audio = rec.listen(source)  
    try:      
        order = rec.recognize_google(audio, language = 'en-US').lower()
        print(f"You: {order}\n")
        return order    
    except Exception as e:
        print(f"{botname}: Can't hear what you saying.\n") 
        order = "None"
        return order   

def speak(speech): # this is the voice of the assistant 
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 200)
    engine.say(speech)
    engine.runAndWait()
     
def get_time(): # this function returns the present hour
    samay = datetime.datetime.now()
    hour = samay.hour
    return hour

def news(): # this function gives the current headings of the news from India Today website
    url = "https://www.indiatoday.in"
    resosponse = requests.get(url)
    soup = bs4.BeautifulSoup(resosponse.text, 'html.parser')
    headlines = soup.find('body').find_all('h3')
    for i in headlines:
        print(f"{botname}: {i.text.strip()}.\n")
        speak(i.text.strip())


hour = get_time() # gets the hour
date = Calender.tarikh() # gets the date
event_day = Calender.event_func() # gets the event name according to the date as programmed
day = Calender.day() # gets the day name       
botname = "Friday" # this the name of the assistant
isplaying = False

def greeting(): # this function is used to greet the user according to time, day and event
    if(event_day != "None"):
        if(hour < 12 or hour == 12):
            print(f"{botname}: Good Morning boss. It's {event_day}. How can i help you?\n")
            speak(f"Good morning boss. It's {event_day}. How can i help you?")
        elif(hour > 12 and hour < 18):
            print(f"{botname}: Good afternoon boss.It's {event_day}. How can i help you?\n")
            speak(f"Good afternoon boss. It's {event_day}. How can i help you?")
        elif(hour > 18 or hour == 18):
            print(f"{botname}: Good evening boss. It's {event_day}. How can i help you?\n")
            speak(f"Good evening boss. It's {event_day}. How can i help you?")
    elif(event_day == "None"):  
        if(hour < 12 or hour == 12):
            print(f"{botname}: Good Morning boss. How can i help you?\n")
            speak(f"Good morning boss. How can i help you?")
        elif(hour > 12 and hour < 18):
            print(f"{botname}: Good afternoon boss. How can i help you?\n")
            speak(f"Good afternoon boss. How can i help you?")
        elif(hour > 18 or hour == 18):
            print(f"{botname}: Good evening boss. How can i help you?\n")
            speak(f"Good evening boss. How can i help you?")      

def assistant(): # this is the main body of the program. This function defines all the command and their works.
    greeting() # greets the user
    while(True):
            hour = get_time()
            data2 = audio_input().lower() # gets the command fro the user and store that into the variable
            if(("play music" in data2)): # plays music
                print(f"{botname}: playing music\n")
                speak("playing music")
                player.play_song()
                isplaying = True
                continue
            elif(("play next" in data2 or "next song" in data2) and isplaying): #if music is playing then it plays the next song.
                player.play_song()
                print(f"{botname}: playing next.\n")
                speak("playing next")
                isplaying = True
                continue
            elif(("stop music" in data2 or "pause" in data2 or "pause music" in data2) and isplaying): #if music is playing then it pauses the song
                player.stop_song()
                print(f"{botname}: music has been stopped.\n")
                speak("music has been stopped")
                isplaying = False
                continue
            elif("open youtube" in data2): #opens the youtube website in your default browser
                speak("opening you tube")
                webbrowser.open("https://www.youtube.com")
                print(f"{botname}: youtube has been opened successfully.\n")
                speak("youtube has been opened successfully")
                continue   
            elif("what is your name" in data2): # to know the name of the assistant
                print(f"{botname}: My name is {botname}. A personal assistant of Mr. AJ.\n")
                speak(f"My name is {botname}. A personal assistant of Mr. AJ.")
                continue
            elif("what is the time" in data2): # to know the current time
                time_now = datetime.datetime.now()
                hour = time_now.hour
                minute = time_now.minute
                if(hour > 12):
                    hour = hour - 12
                print(f"{botname}: It is {hour}'o clock and {minute} minutes.\n")
                speak(f"It is {hour}'o clock and {minute} minutes.")
                continue
            elif("what is the day" in data2): # to know the present day name
                print(f"{botname}: Today is {day}\n")
                speak(f"Today is {day}")
                continue
            elif("what is the date" in data2): # to know the present date
                print(f"{botname}: Today is {date}\n")
                speak(f"Today is {date}")
                continue
            elif("event" in data2): # to know the present event listed for the present date
                print(f"{botname}: Today is {date}")
                speak(f"Today is {date}")
            elif(f"how are you {botname}" in data2): # a programmed conversation
                print(f"{botname}: I am fine. Thank you for asking.\n")
                speak("I am fine. Thank you for asking.")
                continue 
            elif("search in google" in data2): # takes the searching content and searches in google
                google_query = data2[16 :]
                google = "https://www.google.com/search?q="
                speak(f"searching for {google_query}") 
                webbrowser.open(google + google_query)
                speak(f"Here is what i found in google:")
                continue
            elif("shutdown the system" in data2): # to shutdown the pc remotely
                print(f"{botname}: Ok boss, the system will be shut down. Now i will take my leave. Have a nice day boss.")
                speak("Ok boss, the system will be shut down. Now i will take my leave. Have a nice day boss.")
                os.system("shutdown /s")
                break
            elif(f"bye friday" in data2 or f"buy friday" in data2 or f"bi friday" in data2 or f"shutdown friday" in data2 or f"by friday" in data2): # to shutdown the assistant remotely
                if(hour < 19):
                    print(f"{botname}: I am shutting myself down. Have a nice day boss.\n")
                    speak("I am shutting myself down. Have a nice day boss.")
                    isshutdown = True
                    return isshutdown
                elif(hour > 19 or hour == 19):
                    print(f"{botname}: I am shutting myself down. Good night boss.\n")
                    speak("I am shutting myself down. Good night boss.")  
                    isshutdown = True
                    return isshutdown
            elif("search in wikipedia" in data2): # takes the searching content and searches in wikipedia
                wiki_query = data2[19:]
                speak(f"searching for {wiki_query}")
                wiki_result = wikipedia.summary(wiki_query, sentences = 2)
                wikipedia.page(wiki_query)
                print(f"{botname}: Here is what i find in wikipedia. {wiki_result}.") 
                speak(f"Here is what i find in wikipedia. {wiki_result}.")
                 
                continue   
            elif("open wikipedia" in data2): # opens the official wikipedia website in your default browser
                speak("opening wikipedia")
                webbrowser.open("http://www.wikipedia.org")
                print(f"{botname}: wikipedia has opened successfully.\n")
                speak("wikipedia has been opened successfully.")
                continue 
            elif(f"thank you {botname}" in data2): # a programmed conversation
                print(f"{botname}: your welcome boss. I am always at your sevice.")
                speak("your welcome boss. I am always at your sevice.")
                continue
            elif("send email" in data2 or "send mail" in data2): # this senda email to a person the user wanted to
                speak("whom do i send the email? Type the email id.")
                receiver_email = input(f"{botname}: Enter the email id of the receiver here: \n")
                speak("what message should i give him")
                data2 = audio_input()
                user_id = "atanughosh.brp@gmail.com"
                passwordis = "irvzndhcjscbludk"
                content = ""
                with yagmail.SMTP(user_id, passwordis) as yag:
                    speak("sending email")
                    yag.send(receiver_email, data2, content)
                print(f"{botname}: email sent successfully.\n")
                speak("email sent successfully")
                continue    
            elif("search in youtube" in data2): # seaches user query in youtube
                youtube_query = data2[17 :]
                speak(f"searching for {youtube_query}")
                webbrowser.open(f"http://www.youtube.com/results?search_query={youtube_query}")
                speak("here is what i found in youtube:") 
                continue   
            elif("play" in data2): # to play video in youtube by telling the video title
                youtube_query = data2[4 :]
                pywhatkit.playonyt(youtube_query)
                print(f"{botname}: Playing {youtube_query}.\n")
                speak(f"playing {youtube_query}.")
                continue
            elif("write" in data2): # to write down any passage into text file
                print(f"{botname}: What should i give the name of the file:\n")
                speak("What should i give the name of the file:")
                filenam = audio_input()
                file = open(f"{filenam}.txt", "w")
                print(f"{botname}: should i write the current date and time in the file:\n")
                speak("should i write the current date and time in the file:")
                d_t = audio_input()
                print(f"{botname}: What should i write:\n")
                speak("What should i write:")
                writing = audio_input()
                if(d_t == "yes" or d_t == "sure"):
                    current_date = str(datetime.datetime.now())
                    file.write(current_date)
                    file.write(":-")
                    file.write("\n")
                    file.write(writing)
                    print(f"{botname}: writing note is completed")
                    speak("writing note is completed")
                else:
                    file.write(writing)    
                    print(f"{botname}: writing note is completed")
                    speak("writing note is completed")
                file.close()
                continue
            elif("tell a joke" in data2 or "tell us a joke" in data2): # to get a joke from python built in module and tells the joke 
                joke = pyjokes.get_joke()
                print(f"{botname}: {joke}")
                speak(joke)
                continue
            elif("launch vlc" in data2): # launches vlc media player
                speak("launching vlc")
                subprocess.Popen(r"C:\Program Files\VideoLAN\VLC\vlc.exe")
                print(f"{botname}: VLC Media Player has been launched successfully.\n")
                speak("VLC Media Player has been launched successfully")
                continue
            elif("restart the system" in data2): # to restart the pc remotely
                print(f"{botname}: Ok boss, the system will be restarted.\n")
                speak("Ok boss, the system will be restarted.")
                os.system("shutdown /r")
                break
            elif("hibernate the system" in data2): # to hibernate the pc remotely
                print(f"{botname}: Ok sir, the system will be gone to hibernate.\n")
                speak("Ok sir, the system will be gone to hibernate.")
                os.system("shutdown /h")
                print(f"{botname}: The System has been started successfully.")
                speak("The System has been started successfully")
            elif("log out" in data2):
                print(f"{botname}: Ok boss, logging out from our current microsoft account.\n")
                speak("Ok boss, logging out from our current microsoft account")
                os.system("shutdown /l")
                print(f"{botname}: The System has been started successfully.\n")
                speak("The System has been started successfully")
            elif("empty recycle bin" in data2): # to delete all files in recycle bin
                speak("processing")
                winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
                print(f"{botname}: Everything has been deleted from the recycle bin.\n")
                speak("Everything has been deleted from the recycle bin.")
                continue
            elif("launch opera" in data2): # to launch opera gx browser
                speak("launchig opera")
                subprocess.Popen(r"C:\Users\atanu\AppData\Local\Programs\Opera GX\launcher.exe")
                print(f"{botname}: Opera has been successfully launched.\n")
                speak("Opera has been successfully launched.\n")
                continue
            elif("open amazon" in data2): # opens amazon's official website in your default browser
                speak("opening amazon")
                webbrowser.open("http://www.amazon.in")
                print(f"{botname}: Amazon has been successfully opened.\n")
                speak("Amazon has been successfully opened.")
                continue
            elif("open flipkart" in data2): # opens amazon's official website in your default browser
                speak("opening flipkart")
                webbrowser.open("http://www.flipkart.com")
                print(f"{botname}: Flipkart has been successfully opened.\n")
                speak("Flipkart has been successfully opened.")  
                continue 
            elif("open mail" in data2 or "open email" in data2): # to open the gmail in browser
                speak("opening gmail")
                webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
                print(f"{botname}: Gmail has been successfully opened.\n")
                speak("Gmail has been successfully opened.")  
                continue 
            elif("launch steam" in data2): # launches steam
                speak("launching steam")
                subprocess.Popen(r"C:\Program Files (x86)\Steam\steam.exe")
                print(f"{botname}: Steam has been successfully launched.\n")
                speak("steam has been successfully launched.")
                continue  
            elif("launch unity" in data2): # launches unity
                speak("launching unity")
                subprocess.Popen(r"C:\Program Files\Unity Hub\Unity Hub.exe")
                print(f"{botname}: Unity has been successfully launched.\n")
                speak("Unity has been successfully launched.")
                continue    
            elif("launch bluestacks" in data2): # launches bluestacks
                speak("launching bluestacks instance nougat 32 bit")
                subprocess.Popen(r"C:\Program Files\BlueStacks_nxt\HD-Player.exe --instance Nougat32")
                print(f"{botname}: Bluestacks has been successfully launched.\n")
                speak("Bluestacks has been successfully launched.")
                continue 
            elif("launch bluestacks 1" in data2):
                speak("launching bluestacks instance nougat 64 bit")
                subprocess.Popen(r"C:\Program Files\BlueStacks_nxt\HD-Player.exe --instance Nougat64")
                print(f"{botname}: Bluestacks has been successfully launched.\n")
                speak("Bluestacks has been successfully launched.")
                continue
            elif("launch bluestacks 2" in data2):
                speak("launching bluestacks instance pie 64 bit beta")
                subprocess.Popen(r"C:\Program Files\BlueStacks_nxt\HD-Player.exe --instance Pie64 bit(beta)")
                print(f"{botname}: Bluestacks has been successfully launched.\n")
                speak("Bluestacks has been successfully launched.")
                continue
            elif("launch bluestacks multi instance manager" in data2):
                speak("launching bluestacks multi instance manager")
                subprocess.Popen(r"C:\Program Files\BlueStacks_nxt\HD-MultiInstanceManager.exe")
                print(f"{botname}: Bluestacks Multi Instance Manager has been successfully launched.\n")
                speak("Bluestacks Multi Instance Manager has been successfully launched.")
                continue
            elif("how are you" in data2): # a programmed conversation
                print(f"{botname}: I am fine boss. Thank you for asking. How are you?\n")
                speak("I am fine boss. Thank you for asking. How are you?")
                continue
            elif("i am fine" in data2 or "i am good" in data2 or "i am nice" in data2): # a programmed conversation
                print(f"{botname}: It's nice to hear that you are fine.\n")
                speak("It's nice to hear that you are fine.")
                continue
            elif("i am not fine" in data2 or "i am not good" in data2): # a programmed conversation
                print(f"{botname}: what is disturbing you? Can i do something that will make you feel good?\n")
                speak("what is disturbing you? Can i do something that will make you feel good?")
                continue
            elif("what is the headlines" in data2 or "what is in the news" in data2): # gives the headlines of current news from India Today
                news()
                continue
            elif("open news" in data2): # opens the official website of India Today
                speak("opening india today")
                webbrowser.open("https://www.indiatoday.in")
                print(f"{botname}: India Today has successfully launched.\n")
                speak("India Today has been successfully launched")
                continue
            elif("stop listening" in data2 or f"{botname} sleep" in data2): # turn the assistant to sleep for 15 minutes
                print(f"{botname}: ok boss, I am going to sleep for 15 minutes.\n")
                speak("ok boss, I am going to sleep for 15 minutes")
                time.sleep(15*60)
                print("Jarvis: I am awake boss.\n")
                speak("I am awake boss.")
                continue
            elif("launch vs code" in data2 or "launch visual studio" in data2): # launches visual studio
                print(f"{botname}: launching visual studio.\n")
                speak("launching visual studio.")
                subprocess.Popen(r"C:\Users\atanu\AppData\Local\Programs\Microsoft VS Code\Code.exe")
                print(f"{botname}: visual studio has been successfully launched.\n")
                speak("visual studio has been successfully launched.")
                continue
            elif("you are beautiful" in data2): # a programmed conversation
                print(f"{botname}: Thankyou boss, i am flattered.\n")
                speak("Thankyou boss, i am flattered.")
                continue
            elif("will you be my girlfriend" in data2): # a programmed conversation
                print(f"{botname}: I wish i could be. But i am not a human. So i am sorry.\n")
                speak("I wish i could be. But i am not a human. So i am sorry.")
                continue


if(__name__ == "__main__"):
    while(True):
        isconnected = True
        try:
            import pywhatkit 
            if(isconnected):
                data1 = audio_input()
                if("friday" in data1):
                    isshutdown = assistant() 
                    if(isshutdown == True):
                        break
                else: # if the user gives no response then the assistant takes the command as none. 
                    print(f"{botname}: Say the keyword to awake the assistant.\n") 

        except Exception as e:

            print(f"{botname}: You are not connected to Internet.\n")
            speak("You are not connected to Internet.")
            break

            

            
            

       