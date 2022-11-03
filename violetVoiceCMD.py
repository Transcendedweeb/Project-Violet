import threading, datetime
import speech_recognition as sr

import violetAi as AI

listner_list = ["green"]

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone(device_index=1) as source:
        while True:
            print("\nstart\n")
            audio = r.record(source, duration=8)
            r.adjust_for_ambient_noise(source)

            print("\nmiddle\n")
            try:
                listner_list[0] = "red"
                said = r.recognize_google(audio, language="en-us")
                log_file = open("AIconfig\\logs.txt", "a")
                moment_in_time = str(datetime.datetime.now().time())
                log_file.write("["+moment_in_time[0:7]+"] " + "sound found: " + "\"" + said + "\"" + "\n\n")
                log_file.close()
                AI.decoder(said)
            except:
                print("Exception: _404 sound not found")
                log_file = open("AIconfig\\logs.txt", "a")
                moment_in_time = str(datetime.datetime.now().time())
                log_file.write("["+moment_in_time[0:7]+"] " + "Error 001: no sound found.\n\n")
                log_file.close()

            print("\nend\n")
            listner_list[0] = "green"    

def threadVoice():
    a = threading.Thread(target=get_audio)
    a.setDaemon(True)
    a.start()

# print("\n\nstarting\n")
# threadVoice()