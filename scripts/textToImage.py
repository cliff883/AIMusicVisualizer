from dalle2 import Dalle2
from PIL import Image

def textToImage(phrases):
    print(phrases)
    dalle = Dalle2("sess-7j1ChQvHS3mXvYC6Llxft4TzBzVZYfltUoAmtADX") # your bearer key
    for i in range(len(phrases)):
        generations = dalle.generate(phrases[i])
        file_paths = dalle.generate_and_download(phrases[i])
        print(generations)
        print(file_paths)
        im = Image.open(generations[0]['id'] + ".webp").convert("RGB")
        im.save("image" + str(i) + ".jpg")
#textToImage()