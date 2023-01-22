import tkinter
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
from ecapture import ecapture as ec
import wolframalpha
import json
import requests
    

print('Loading your AI personal assistant - SENTINEL')

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice','voices[0].id')


def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Hello,Good Morning")
        print("Hello,Good Morning")
    elif hour>=12 and hour<18:
        speak("Hello,Good Afternoon")
        print("Hello,Good Afternoon")
    else:
        speak("Hello,Good Evening")
        print("Hello,Good Evening")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source)

        try:
            statement=r.recognize_google(audio,language='en-in')
            print(f"user said:{statement}\n")

        except Exception as e:
            speak("Pardon me, please say that again")
            return "None"
        return statement

speak("Loading your AI personal assistant SENTINELL")
wishMe()




def result_window(event=None):
    def destroy_result_window(event=None):
        query_result_window.destroy()
    query_result_window=tkinter.Toplevel()
    query_result_window.minsize(400,400)
    query_result_window.maxsize(400,400)
    tkinter.Label(query_result_window,bg="#95a5a6",height=400,width=400).place(x=0,y=0)
    result = tkinter.Text(query_result_window,height=18,width=47,bg="#d0d3d4")
    result.place(x=10,y=40)
    user_input=query_input.get()
    # --------------------------------------
    if __name__=='__main__':
            while True:
                speak("Tell me how can I help you now?")
                statement = takeCommand().lower()
                if statement==0:
                    continue

                if "good bye" in statement or "ok bye" in statement or "stop" in statement or "goodbye" in statement:
                    speak('your personal assistant sentinel is shutting down,Good bye')
                    print('your personal assistant sentinel is shutting down,Good bye')
                    break



                if 'wikipedia' in statement:
                    try:
                        speak('Searching Wikipedia...')
                        statement =statement.replace("wikipedia", "")
                        results = wikipedia.summary(statement, sentences=3)
                        speak("According to Wikipedia")
                        print(results)
                        speak(results)
                    except :
                        speak("Sorry the word was not found")
                        pass

                elif 'open youtube' in statement:
                    webbrowser.open_new_tab("https://www.youtube.com")
                    speak("youtube is open now")
                    time.sleep(5)

                elif 'open google' in statement:
                    webbrowser.open_new_tab("https://www.google.com")
                    speak("Google chrome is open now")
                    time.sleep(5)

                elif 'open gmail' in statement:
                    webbrowser.open_new_tab("gmail.com")
                    speak("Google Mail open now")
                    time.sleep(5)

                elif "weather" in statement:
                    api_key="88f5f13c013472752146a867d3a5d6a4"
                    base_url="https://api.openweathermap.org/data/2.5/weather?"
                    speak("whats the city name")
                    city_name=takeCommand()
                    complete_url=base_url+"appid="+api_key+"&q="+city_name
                    response = requests.get(complete_url)
                    x=response.json()
                    if x["cod"]!="404":
                        y=x["main"]
                        current_temperature = y["temp"]
                        current_humidiy = y["humidity"]
                        z = x["weather"]
                        weather_description = z[0]["description"]
                        speak(" Temperature in kelvin unit is " +
                            str(current_temperature) +
                            "\n humidity in percentage is " +
                            str(current_humidiy) +
                            "\n description  " +
                            str(weather_description))
                        print(" Temperature in kelvin unit = " +
                            str(current_temperature) +
                            "\n humidity (in percentage) = " +
                            str(current_humidiy) +
                            "\n description = " +
                            str(weather_description))

                    else:
                        speak(" City Not Found ")



                elif 'time' in statement:
                    strTime=datetime.datetime.now().strftime("%H:%M:%S")
                    speak(f"the time is {strTime}")

                elif 'who are you' in statement or 'what can you do' in statement:
                    speak('Sentinal,your persoanl assistant. I am programmed to minor tasks like'
                        'opening youtube,google chrome,gmail and stackoverflow ,predict time,take a photo,search wikipedia,predict weather' 
                        'in different cities , get top headline news from times of india and you can ask me computational or geographical questions too!')


                elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
                    speak("I was built by Jeetendra")
                    print("I was built by Jeetendra")

                elif "open stackoverflow" in statement:
                    webbrowser.open_new_tab("https://stackoverflow.com/login")
                    speak("Here is stackoverflow")

                elif 'news' in statement:
                    news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
                    speak('Here are some headlines from the Times of India,Happy reading')
                    time.sleep(6)

                elif "camera" in statement or "take a photo" in statement:
                    ec.capture(0,"robo camera","img.jpg")

                elif 'search'  in statement:
                    statement = statement.replace("search", "")
                    webbrowser.open_new_tab(statement)
                    time.sleep(5)

                elif 'answer' in statement:
                    speak('I can answer to computational and geographical questions and what question do you want to ask now')
                    question=takeCommand()
                    app_id="3T9EJV-87RKVAG2AJ"
                    client = wolframalpha.Client('3T9EJV-87RKVAG2AJ')
                    res = client.query(question)
                    answer = next(res.results).text
                    speak(answer)
                    print(answer)


                elif "log off" in statement or "sign out" in statement or "shut down" in statement or "shutdown" in statement:
                    speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
                    subprocess.call(["shutdown", "/l"])

    time.sleep(3)


        


       

   
    
    tkinter.Button(query_result_window,text="Close",command=query_result_window.destroy,font=("Comic Sans MS", 10), width = 8,bg="#808b96").place(x=310,y=350)
    query_result_window.bind('<Escape>', destroy_result_window)
def destroy_root(event=None):
    root.destroy()
def clear_text():
    query_input.delete(0,'end')
root = tkinter.Tk()
root.title("SENTINEL")
logo=tkinter.PhotoImage(file="C:\\Users\\jeete\\OneDrive\\Desktop\\sentinel\\logo.gif")
root.minsize(400,400)
root.maxsize(400,400)
root.geometry("400x400")
logo_va=tkinter.Label(root,image=logo,height=400,width=400,bg="#95a5a6").place(x=0,y=0)
query_label=tkinter.Label(root, text="Listening",font=("Comic Sans MS", 12),bg="#d0d3d4")
query_label.place(x=0,y=100)
query_input=tkinter.Entry(root,font=("Comic Sans MS", 12),bg="#d0d3d4")
query_input.place(x=200,y=135)
tkinter.Button(root,text="CLOSE",command=root.destroy,font=("Comic Sans MS", 10), width = 8,bg="#808b96").place(x=90,y=350)
tkinter.Button(root,text="START",command=result_window,font=("Comic Sans MS", 10), width = 8,bg="#808b96").place(x=230,y=350)
root.bind('<Return>', result_window)
root.bind('<Escape>', destroy_root)
root.mainloop()