import speech_recognition as sr
def calculate_error_rate(actual_transcript, recognized_transcript):
 actual_words = actual_transcript.split()
 recognized_words = recognized_transcript.split()
 errors = sum(1 for actual, recognized in zip(actual_words,
recognized_words) if actual != recognized)
 error_rate = errors / len(actual_words) if len(actual_words) > 0 else 0
 return error_rate
def recognize_speech(audio_file):
 recognizer = sr.Recognizer()
 with sr.AudioFile(audio_file) as source:
  audio_data = recognizer.record(source)
 try:
  recognized_text = recognizer.recognize_google(audio_data)
  return recognized_text
 except sr.UnknownValueError:
  return "Speech recognition could not understand audio"
 except sr.RequestError as e:
  return "Error occurred during recognition: {0}".format(e)
audio_file_path = "/content/sample-9s.mp3"
actual_transcript = "This is an example transcript for testing the speech recognition system."
recognized_transcript = recognize_speech(audio_file_path)
error_rate = calculate_error_rate(actual_transcript,
recognized_transcript)
print("Actual Transcript:", actual_transcript)
print("Recognized Transcript:", recognized_transcript)
print("Error Rate:", error_rate)
