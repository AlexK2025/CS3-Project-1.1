from random import *
import time
import json

with open("questions.json", "r") as f:
    questions = json.load(f)

def back(num):
    for i in range(num):
        print('\033[F\33[2K', end='')

def main():
    back(2)
    score = 0
    while True:
        back(1)
        key = f"{randrange(9) + 1}"
        print(questions[key]["q"])
        for item in questions[key]["l"]:
            print(item)
        answer = input()
        if answer != questions[key]["a"]:
            break
        score += 1
        back(6)
        print(f"yay! score: {score}")
        time.sleep(2)
    back(6)
    print(f"YOU SUCK!!! final score: {score}")

if __name__ == "__main__":
    main()