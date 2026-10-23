import json

questions = {
    "what is the capital of france?": ["Paris", "Toulouse", "Lyon"],
    "what is the capital of germany?": ["Berlin", "Hamburg", "Munich"],
    "what is the capital of italy?": ["Rome", "Milan", "Naples"],
    "what is the capital of spain?": ["Madrid", "Barcelona", "Seville"],
    "what is the capital of japan?": ["Tokyo", "Kyoto", "Osaka"],
    "what is the capital of canada?": ["Ottawa", "Toronto", "Vancouver"]
}

fileName = "quizQuestions.json"

with open(fileName, "w") as file:
    json.dump(questions, file, indent=4)

print(f"Quiz questions have been saved to {fileName}.")