from flask import Flask, redirect, render_template, request, session
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
# Load Scores
# -------------------------
def load_scores():

    filename = "scores.json"

    if not os.path.exists(filename):
        return []

    with open(filename, "r") as file:
        return json.load(file)

# -------------------------
# Save Score
# -------------------------
def save_score(score):

    filename = "scores.json"
    scores = load_scores()

    scores.append(score)

    with open(filename, "w") as file:
        json.dump(scores, file, indent=4)

# -------------------------
# Load High Score
# -------------------------
def get_high_score():

    scores = load_scores()
    return max(scores) if scores else 0

# -------------------------
# Leaderboard
# -------------------------
@app.route("/leaderboard")
def leaderboard():
    scores = sorted(load_scores(), reverse=True)
    return render_template("leaderboard.html", scores=scores)


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
    session["quiz_finished"] = False

    return render_template("quiz.html", question=quiz[0], question_number=1, total=len(quiz))

# -------------------------
# Next Question
# -------------------------
@app.route("/next")
def next_question():

    quiz = session.get("quiz")
    current = session.get("current", 0)

    if not quiz or current >= len(quiz) or session.get("quiz_finished"):
        return redirect("/")

    return render_template(
        "quiz.html",
        question=quiz[current],
        question_number=current + 1,
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

    finished = session["current"] >= len(quiz)

    if finished:
        score = session["score"]

        duration = round(
            time.time() - session["start_time"],
            2
        )

        session["quiz_finished"] = True
        session["duration"] = duration
        save_score(score)

        return render_template(
            "explanation.html",
            feedback=feedback,
            question_number=current + 1,
            total=len(quiz),
            finished=True
        )

    return render_template(
        "explanation.html",
        feedback=feedback,
        question_number=current + 1,
        total=len(quiz),
        finished=False
    )

# -------------------------
# Results Page
# -------------------------
@app.route("/results")
def results():
    if not session.get("quiz_finished"):
        return redirect("/")

    return render_template(
        "results.html",
        score=session["score"],
        high_score=get_high_score(),
        duration=session["duration"]
    )

if __name__ == "__main__":
    app.run(debug=True)