from random import *
import time

score = 0
questions = [
    {
        "q": "who was to alex's right on 9/19/2024 at 2:12 pm", 
        "a": "hendrix",
        "l": ["hendrix", "sohan", "grace", "lucian"]
    },
    {
        "q": "what is pokemon 150", 
        "a": "mew",
        "l": ["mew", "mewtwo", "moltres", "dragonite"]
    },
    {
        "q": "is hotdog a sandwich", 
        "a": "no",
        "l": ["no", "yes", "maybe", "yessir"]
    },
    {
        "q": "i want it", 
        "a": "that way",
        "l": ["that way", "me too", "a lot", "cold"]
    },
    {
        "q": "whos that guy who made that song", 
        "a": "gotye",
        "l": ["gotye", "usher", "flo rida", "rihanna"]
    },
    {
        "q": "whats the last name of the guy who made the turing machine",
        "a": "turing",
        "l": ["turing", "alan", "smith", "zhang"]
    },
    {"q": "did you get the photos printed?",
        "a": "bogos binted? 👽",
        "l": ["bogos binted? 👽", "yes", "no", "sorry :("]
    },
    {
        "q": "cat or dog", 
        "a": "cat",
        "l":  ["cat", "dog", "neither", "feline"]
    },
    {
        "q": "yo sohan give me a question",
        "a": "what would sohan say if he was asked \"hey sohan give me a questions\"",
        "l": ["what would sohan say if he was asked \"hey sohan give me a questions\"", "no", "shut up", "ok"]
    },
    {
        "q": "what would sohan say if he was asked \"hey sohan give me a questions\"",
        "a": "idk",
        "l": ["idk", "what would sohan say if he was asked \"hey sohan give me a questions\"", "cheeseburger", "not answering it"]
    },
]

def main():
    while True:
        randKeyNum = randrange(10)
        print(questions[randKeyNum]["q"])
        for item in questions[randKeyNum]["l"]:
            print(item)
        answer = input()
        if answer == questions[randKeyNum]["a"]:
            print("yay!")
            time.sleep(2)
        else:
            break
        print('\033[F\33[2K\033[F\33[2K\033[F\33[2K\033[F\33[2K\033[F\33[2K\033[F\33[2K\033[F\33[2K\033[F\33[2K\033[F\33[2K\033[F')
if __name__ == "__main__":
    main()