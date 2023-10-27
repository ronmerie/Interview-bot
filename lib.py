import whisper
from gtts import gTTS

def transcribeAudio(audioName):
    model = whisper.load_model("base")
    result = model.transcribe(f"assets/{audioName}",fp16=False)
    return result['text']

def text_to_speech(text,file):
    tts = gTTS(text)
    tts.save(f'assets/{file}.mp3')
    