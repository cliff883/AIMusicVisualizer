import whisper
def main():
    model = whisper.load_model("base")
    audio = model.transcribe("Fly_Me_to_the_Moon.mp3")
    print(audio["text"])
main()