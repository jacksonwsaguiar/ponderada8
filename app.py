import argparse
import speech_recognition as sr

from gtts import gTTS
from translate import Translator

translator= Translator(to_lang="pt")


def upload_audio(file_path):
    r = sr.Recognizer()
    try:

        with sr.AudioFile(file_path) as source:
            audio_text = r.listen(source)
    
            text = r.recognize_google(audio_text)
            print('Converting audio transcripts into text ...')
            print(text)

            print("----------------------------------")

            translation = translator.translate(text)
            print('Translate...')
            print(translation)
            
            print("----------------------------------")
            
            tts = gTTS(translation, lang='pt', tld='com.br')
            print('Saving audio...')
            tts.save('output.mp3')
         

     
    except Exception as e:
        print(f"Erro ao carregar o arquivo de áudio: {str(e)}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Receber um arquivo de áudio.")
    parser.add_argument("file_path", type=str, help="Caminho para o arquivo de áudio")

    args = parser.parse_args()

    upload_audio(args.file_path)
