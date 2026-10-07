#interactive quiz system, version3
#make a dictionary with the questions and correct answers

questions = {
    "what is the capital of france?": ["Paris", "Toulouse", "Lyon"],
    "what is the capital of germany?": ["Berlin", "Hamburg", "Munich"],
    "what is the capital of italy?": ["Rome", "Milan", "Naples"]
}

for question, answers in questions.items():
    correctAnswer = answers[0]
    answer = input(f"{question} ")
    for answer in answers:
        print(f"- {answer}")

    if answer == correctAnswer:
        print("correct")
    else:
        print(f"the asnwer is '{correctAnswer}', not {answer!r}")