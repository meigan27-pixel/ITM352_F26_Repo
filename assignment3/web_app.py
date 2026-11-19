from flask import Flask, render_template, request, jsonify, session
from string import ascii_lowercase
import random
import json
import time
import os

app = Flask(__name__)
app.secret_key = "quiz_secret_key"

NUM_QUESTIONS_PER_QUIZ = 5

# -------------------------
# Load Questions
# -------------------------
def load_questions():
    with open("questions.json", "r") as file:
        return json.load(file)

# -------------------------
# Original Function Adapted
# -------------------------
def prepareQuestions(questions, numQuestions):
    numQuestions = min(numQuestions, len(questions))
    return random.sample(list(questions.items()), k=numQuestions)

# -------------------------
# Save Score
# -------------------------
def save_score(score):

    filename = "scores.json"

    if os.path.exists(filename):
        with open(filename, "r") as file:
            scores = json.load(file)
    else:
        scores = []

    scores.append(score)

    with open(filename, "w") as file:
        json.dump(scores, file, indent=4)

# -------------------------
# Load High Score
# -------------------------
def get_high_score():

    filename = "scores.json"

    if not os.path.exists(filename):
        return 0

    with open(filename, "r") as file:
        scores = json.load(file)

    return max(scores) if scores else 0


# -------------------------
# Home Page
# -------------------------
@app.route("/")
def home():
    return render_template("index.html")

# -------------------------
# Start Quiz
# -------------------------
@app.route("/start")
def start_quiz():

    questions = load_questions()

    selected_questions = prepareQuestions(
        questions,
        NUM_QUESTIONS_PER_QUIZ
    )

    quiz = []

    for question, data in selected_questions:

        choices = data["choices"]

        correct_answer = choices[0]

        shuffled_choices = random.sample(
            choices,
            len(choices)
        )

        quiz.append({
            "question": question,
            "choices": shuffled_choices,
            "correct": correct_answer,
            "explanation": data["explanation"]
        })

    session["quiz"] = quiz
    session["score"] = 0
    session["current"] = 0
    session["start_time"] = time.time()

    return render_template(
        "quiz.html",
        question=quiz[0],
        question_number=1,
        total=len(quiz)
    )

# -------------------------
# Submit Answer
# -------------------------
@app.route("/submit", methods=["POST"])
def submit():

    answer = request.form.get("answer")

    current = session["current"]

    quiz = session["quiz"]

    current_question = quiz[current]

    feedback = {}

    if answer == current_question["correct"]:

        session["score"] += 1

        feedback["correct"] = True

    else:

        feedback["correct"] = False

    feedback["correct_answer"] = current_question["correct"]

    feedback["explanation"] = current_question["explanation"]

    session["current"] += 1

    if session["current"] >= len(quiz):

        score = session["score"]

        duration = round(
            time.time() - session["start_time"],
            2
        )

        save_score(score)

        return jsonify({
            "finished": True,
            "score": score,
            "high_score": get_high_score(),
            "duration": duration,
            "feedback": feedback
        })

    next_question = quiz[session["current"]]

    return jsonify({
        "finished": False,
        "feedback": feedback,
        "question": next_question,
        "number": session["current"] + 1
    })

# -------------------------
# Results Page
# -------------------------
@app.route("/results")
def results():
    return render_template("results.html")

if __name__ == "__main__":
    app.run(debug=True)