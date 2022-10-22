import whisper
import re
from textToImage import textToImage

def main():
    model = whisper.load_model("base")
    audio = model.transcribe("Fly_Me_to_the_Moon.mp3")
    phrases = re.split(r"[,.]", audio["text"])
    textToImage(phrases)
main()