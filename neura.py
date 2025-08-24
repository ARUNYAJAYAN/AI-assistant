import speech_recognition as sr

class Neura:
    def __init__(self):
        self.name = "Neura"
    def listen(self):
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            audio = recognizer.listen(source)
            return recognizer.recognize_google(audio)
    def response(self):
        user_input = self.listen()
        if "hello" in user_input.lower():
            return f"Hello! I am {self.name}. How can I assist you today?"
        elif "how are you" in user_input.lower():
            return "I'm great, thanks! How about you?"
        else:
            return "I'm not sure how to respond to that. Can you ask something else?"
nove = Neura()
print(nove.response())
