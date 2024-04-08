from transformers import AutoTokenizer, BlenderbotForConditionalGeneration
import speech_recognition as sr
import pyttsx3

#global
mname = "facebook/blenderbot-400M-distill"
model = BlenderbotForConditionalGeneration.from_pretrained(mname)
tokenizer = AutoTokenizer.from_pretrained(mname)
def SpeakText(command):
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()
def chat(user_input):
    inputs = tokenizer([user_input], return_tensors="pt")
    reply_ids = model.generate(**inputs)
    reply=tokenizer.batch_decode(reply_ids, skip_special_tokens=True)[0]
    print(f"Bot>> {reply}")
    SpeakText(reply)

def speechtotext(r):
    # use the microphone as source for input.
    with sr.Microphone() as source2:
        # wait for a second to let the recognizer
        # adjust the energy threshold based on
        # the surrounding noise level
        r.adjust_for_ambient_noise(source2, duration=0.2)
        print('Speak....')
        # listens for the user's input
        audio2 = r.listen(source2, timeout=10, phrase_time_limit=10)
        print("recognising....")
        # Using google to recognize audio
        MyText = r.recognize_google(audio2)
        MyText = MyText.lower()

        return MyText
def speechinit():
        r = sr.Recognizer()
        # Exception handling to handle
        # exceptions at the runtime
        try:
            text=speechtotext(r)
            return text
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
            print("Lets retry")
            text=speechtotext(r)
            return text

        except sr.UnknownValueError:
            print("unknown error occurred")
            print("Lets retry")
            text = speechtotext(r)
            return text


def main():

    while(True):
        choice=input("Enter 1 for keyboard and 2 for mic")
        if choice=='1':
            user_input = input("You>> ")
            if user_input.lower() in ['bye', 'quit', 'terminate']:
                break;
            chat(user_input)
        elif choice=='2':
            user_input=speechinit()
            if user_input.lower() in ['bye', 'quit', 'terminate']:
                break;
            print(f"You>> {user_input}")
            chat(user_input)
        else:
            break

if __name__=="__main__":
    main()

