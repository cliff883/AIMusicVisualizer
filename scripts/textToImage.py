from dalle2 import Dalle2

def textToImage(phrases):
    print(phrases)
    dalle = Dalle2("sess-7j1ChQvHS3mXvYC6Llxft4TzBzVZYfltUoAmtADX") # your bearer key
    for i in range(len(phrases)):
        file_paths = dalle.generate_and_download(phrases[i].strip())
        print(file_paths)
#textToImage()