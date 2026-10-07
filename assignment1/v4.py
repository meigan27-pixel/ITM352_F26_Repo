#interactive quiz system, version4
#make a dictionary with the questions and correct answers
#allow user to choose the option by its label

questions = {
    "what is the capital of france?": ["Paris", "Toulouse", "Lyon"],
    "what is the capital of germany?": ["Berlin", "Hamburg", "Munich"],
    "what is the capital of italy?": ["Rome", "Milan", "Naples"]
}

for question, answers in questions.items():
    correctAnswer = answers[0]
    sortedAnswers = sorted(answers)

    for label, answer in enumerate(sortedAnswers, start=1):
        print(f"{label}. {answer}")

    answerLabel = int(input(f"{question}"))
    answer = sortedAnswers[answerLabel - 1]

    if answer == correctAnswer:
        print("correct")
    else:
        print(f"the asnwer is '{correctAnswer}', not {answer!r}")