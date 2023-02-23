import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    audio = r.listen(source)
    print("Please wait!!!Clearing the background noises!!!")
    r.adjust_for_ambient_noise(source,duration=1)
    print("Soon speech recognition will start,waiting for your message!!")
    print("Please speak now!")
    audio=r.listen(source,timeout=50)
    print("Recording has been completed!!")
try:
    print("Recognizing")
    result=r.recognize_google(audio)
    print(result)
except Exception as ex:
    print(ex)