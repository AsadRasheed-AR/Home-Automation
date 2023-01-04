import sys
import threading
import tkinter as tk
import time

import speech_recognition
import pyttsx3 as tts

from Home_Automation import GenericAssistant

class Assistant:
    def __init__(self):
        self.recognizer = speech_recognition.Recognizer()
        self.speaker = tts.init()
        self.speaker.setProperty("rate", 150)

        self.mappings = {"light on" : self.light_on, "light of" : self.light_of, "fan on": self.fan_on, "fan of": self.fan_of}
        self.assistant = GenericAssistant("intents.json")
        self.assistant.train_model()


        self.root = tk.Tk()
        self.label = tk.Label(text= "BOT", font= {"Arial", 500, "bold"})
        self.label.pack()

        threading.Thread(target=self.run_assistant).start()
        # self.run_assistant()

        self.root.mainloop()

    def light_on(self):
        print("You triggered the light_on intent!")
    
    def light_of(self):
        print("You triggered the light_off intent!")

    def fan_on(self):
        print("You triggered the fan_on intent!")
    
    def fan_of(self):
        print("You triggered the fan_off intent!")

    def run_assistant(self):
        while True:
            try:
                with speech_recognition.Microphone() as mic:
                    self.recognizer.adjust_for_ambient_noise(mic, duration=0.3)
                    audio = self.recognizer.listen(mic)

                    text = self.recognizer.recognize_google(audio)
                    text = text.lower()

                    if "hello" in text:
                        # self.speaker.say("Listning!")
                        # self.speaker.runAndWait()
                        print("Listning >>>")
                        self.label.config(fg="red")
                        audio = self.recognizer.listen(mic)
                        text = self.recognizer.recognize_google(audio)
                        text = text.lower()

                        if text == "stop":
                            self.speaker.say("Bye")
                            self.speaker.runAndWait()
                            self.speaker.stop()
                            self.root.destroy()
                            sys.exit()
                        
                        else:
                            if text is not None:
                                response = self.assistant.request(text)
                                if response is not None:
                                    self.speaker.say(response)
                                    self.speaker.runAndwait()
                                self.label.config(fg="black")
            except:
                self.label.config(fg="black")
                continue

Assistant()

