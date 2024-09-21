from random import *
import time

questions = [
    {
        "q": "who was to alex's right on 9/19/2024 at 2:12 pm", 
        "a": "hendrix",
        "l": ["sohan", "grace", "lucian", "hendrix"]
    },
    {
        "q": "what is pokemon 150", 
        "a": "mew",
        "l": ["mew", "mewtwo", "moltres", "dragonite"]
    },
    {
        "q": "is hotdog a sandwich", 
        "a": "no",
        "l": ["yes", "maybe", "yessir", "no"]
    },
    {
        "q": "i want it", 
        "a": "that way",
        "l": ["me too", "that way", "a lot", "cold"]
    },
    {
        "q": "whos that guy who made that song", 
        "a": "gotye",
        "l": ["flo rida", "usher", "gotye", "rihanna"]
    },
    {
        "q": "whats the last name of the guy who made the turing machine",
        "a": "turing",
        "l": ["smith", "alan", "turing", "zhang"]
    },
    {"q": "did you get the photos printed?",
        "a": "bogos binted? 👽",
        "l": ["yes", "bogos binted? 👽", "no", "sorry :("]
    },
    {
        "q": "cat or dog", 
        "a": "cat",
        "l":  ["dog", "cat", "neither", "feline"]
    },
    {
        "q": "yo sohan give me a question",
        "a": "what would sohan say if he was asked \"hey sohan give me a question\"",
        "l": ["no", "shut up", "what would sohan say if he was asked \"hey sohan give me a question\"", "ok"]
    },
    {
        "q": "what would sohan say if he was asked \"hey sohan give me a question\"",
        "a": "not answering it",
        "l": ["idk", "what would sohan say if he was asked \"hey sohan give me a questions\"", "cheeseburger", "not answering it"]
    },
]

def back(num):
    i = 0
    while i < num:
        print('\033[F\33[2K', end='')
        i+=1

def main():
    back(2)
    score = 0
    while True:
        randKeyNum = randrange(10)
        print(questions[randKeyNum]["q"])
        for item in questions[randKeyNum]["l"]:
            print(item)
        answer = input()
        if answer == questions[randKeyNum]["a"]:
            score += 1
            back(6)
            print(f"yay! score: {score}")
            time.sleep(2)
        else:
            break
        back(7)
    back(6)
    print(f"YOU SUCK!!! final score: {score}")
if __name__ == "__main__":
    main()