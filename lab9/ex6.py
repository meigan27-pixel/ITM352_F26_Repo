#read a file of quiz questions and save as a dictionary

import json

fileName = "quizQuestions.json"

with open(fileName, "r") as file:
    questions = json.load(file)

print(questions)