import speech_recognition as sr
from pydub import AudioSegment
import os


src = "hello.mp3"
dst = "hello.wav"

# convert wav to mp3                                                            
sound = AudioSegment.from_mp3(src)
sound.export(dst, format="wav")

r = sr.Recognizer()

# Open the audio file
with sr.AudioFile("hello.wav") as source:
    audio_text = r.record(source)
# Recognize the speech in the audio
text = r.recognize_google(audio_text, language='en-US')

file_name = "transcription.txt"

with open(file_name, "w") as file:
    # Write to the file
    file.write(text)
# Open the file for editing by the user
os.system(f"start {file_name}")