import speech_recognition as sr
import pyttsx3

class Nova:
    def __init__(self):
        self.name = "Nova"
        self.engine = pyttsx3.init()
    def listen(self):
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            audio = recognizer.listen(source)
            try:
                return recognizer.recognize_google(audio)
            except sr.UnknownValueError:
                print("Sorry, I did not understand that.")
                self.speak("Sorry, I did not understand that. Please try again.")
                return ""
            except sr.RequestError:
                print("Sorry, there was a problem with the speech recognition service.")
                self.speak("Sorry, there was a problem with the speech recognition service.")
                return ""

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()
    def response(self):
        user_input = self.listen()
        if "hello" in user_input.lower():
            reply = f"Hello! I am {self.name}. How can I assist you today?"
        elif "how are you" in user_input.lower():
            reply = "I'm great, thanks! How about you?"
        else:
            reply = "I'm not sure how to respond to that. Can you ask something else?"
        self.speak(reply)
        return reply
nove = Nova()
print(nove.response())

          