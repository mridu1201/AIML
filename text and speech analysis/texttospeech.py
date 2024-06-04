import pyttsx3
import speech_recognition
# Create a text-to-speech engine
engine = pyttsx3.init()
# Convert the text to speech
text = "Hello, world!"
engine.say(text)
engine.runAndWait()
# Save the speech to a file
engine.save_to_file(text, "/content/sample-9s.mp3")
# Create a speech recognition object
r = speech_recognition.Recognizer()
# Convert the speech to text
with open("output.mp3", "rb") as f:
 audio = f.read()
try:
 text = r.recognize_google(audio)
 print("The converted text is:", text)
except Exception as e:
 print("Could not recognize speech:", e)
# Calculate the accuracy
accuracy = len(text) / len(text)
print("The accuracy is:", accuracy)