from flask import Flask
import json
import random


def load_questions():
    with open("questions.json", "r") as file:
        return json.load(file)

def prepare_questions(questions, num_questions):
    num_questions = min(
        num_questions,
        len(questions)
    )

    return random.sample(
        questions,
        k=num_questions
    )

@app.route("/quiz")
def quiz():

    questions = load_questions()

    random_questions = prepare_questions(
        questions,
        5
    )

    return render_template(
        "quiz.html",
        questions=random_questions
    )

app = Flask(__name__)

@app.route("/")
def home():
    return "Quiz Game"

if __name__ == "__main__":
    app.run(debug=True)