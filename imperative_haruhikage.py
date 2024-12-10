def monologue(actor: str, content: str):
    if actor == "Tomori" and content == "あの時...":
        print("This is Scene 1.")
        pass
    else:
        raise NotImplementedError

def play(actor: str, instrument: str, song: str):
    if actor == "Lena" and instrument == "Guitar" and song == "Haruhikage":
        print("This is Scene 2.")
        pass
    elif actor == "Soyo" and instrument == "Bass":
        raise NotImplementedError
    elif actor == "Lena" and instrument == "Piano":
        raise NotImplementedError
    elif  actor == "Lena" and instrument == "Guitar" and song == "Mayoiuta":
        raise NotImplementedError
    elif actor == "Tomori" and instrument == "Angle iron":
        raise NotImplementedError
    elif actor == "Taki" and instrument == "Drum":
        raise NotImplementedError
    else:
        raise NotImplementedError

def why_play_haruhikage():
    monologue("Tomori", "あの時...")
    play("Lena", "guitar", "Haruhikage")

if __name__ == '__main__':
    why_play_haruhikage()   # NotImplementedError

