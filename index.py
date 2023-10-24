from gtts import gTTS
from playsound import playsound
import streamlit as st
import numpy as np
import os

def text_to_speech(text,file):
    tts = gTTS(text)
    tts.save(f'assets/{file}.mp3')
    # playsound(f'assets/{file}.mp3')


data = st.text_input(
    placeholder='Text',
    label='data'
)
file = st.text_input(
    placeholder='File name',
    label='file'
)
st.write(f'text is {data} and file is {file}' )



if st.button('Text to Speech'):
    text_to_speech(data,file)
    audio_file = open(f'assets/{file}.mp3', 'rb')
    audio_bytes = audio_file.read()

    st.audio(audio_bytes, format='audio/ogg')

    sample_rate = 44100  # 44100 samples per second
    seconds = 2  # Note duration of 2 seconds
    frequency_la = 440  # Our played note will be 440 Hz
    # Generate array with seconds*sample_rate steps, ranging between 0 and seconds
    t = np.linspace(0, seconds, seconds * sample_rate, False)
    # Generate a 440 Hz sine wave
    note_la = np.sin(frequency_la * t * 2 * np.pi)
    st.audio(note_la, sample_rate=sample_rate)

# folder path
# dir_path = r'E:\\account\\'

# list to store files name
res = []
for (dir_path, dir_names, file_names) in os.walk('assets/'):
    res.extend(file_names)
st.write(res)

