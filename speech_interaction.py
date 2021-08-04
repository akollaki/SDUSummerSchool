from gtts import gTTS
from io import BytesIO
from pydub import AudioSegment
from pydub.playback import play
import speech_recognition as sr
import re

# Google speech recognition
def google_in(lang):
    r = sr.Recognizer()
    r.pause_threshold = 0.5
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=0.5)
        print("Say something!")
        try:
            audio = r.listen(source, timeout=3, phrase_time_limit=2)
        except sr.WaitTimeoutError:
            return "Timeout"
        else:
            try:
                out = r.recognize_google(audio, language=lang)
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))
            else:
                return out
        return "Error"

# can be used to search for words in string from speech recognition
def find_whole_word(w):
    return re.compile(r'\b({0})\b'.format(w), flags=re.IGNORECASE).search

# text-to-speech
def speak(text):
    with BytesIO() as f: # open buffer f to temporarily store audio
        tts = gTTS(text=text, lang="en") # google text-to-speech
        tts.write_to_fp(f)  # write speech to f
        f.seek(0)  # seek to zero after writing
        audio = AudioSegment.from_file(f, format="mp3") # create audio from buffer
        play(audio) # play audio
