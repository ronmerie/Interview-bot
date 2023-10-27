
import streamlit as st
import os
import numpy as np
import time
from lib import transcribeAudio,text_to_speech


# Tabs
tab1,tab2 = st.tabs(["Text to Speech","Transcribe"])

with tab1:
    data = st.text_input(
        placeholder='Text',
        label='data'
    )
    file = st.text_input(
        placeholder='File name',
        label='file'
    )
    st.write(f'text is {data} and file is {file}' )


    # Button handles converting text to speech
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

with tab2:
    # Loop through assets folder and get all files
    res = []
    for (dir_path, dir_names, file_names) in os.walk('assets/'):
        res.extend(file_names)


    # Transcribe audio
    option = st.selectbox(
        'Choose audio file to transcribe',
        (res)
    )

    st.write("You Chose: ",option)
    if st.button('Transcribe Audio'):
        with st.status("Transcribing...", expanded=True) as status:
            st.write("Transcribing data...")
            data = transcribeAudio(option)
            if data:
                status.update(label="Transcription complete!", state="complete", expanded=False)
        
        st.write(data)
