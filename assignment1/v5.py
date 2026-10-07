#interactive quiz system, version5
#make a dictionary with the questions and correct answers
#allow user to choose the option by its label
#improve usablility and look. keep track of correct answers

from string import ascii_lowercase

questions = {
    "what is the capital of france?": ["Paris", "Toulouse", "Lyon"],
    "what is the capital of germany?": ["Berlin", "Hamburg", "Munich"],
    "what is the capital of italy?": ["Rome", "Milan", "Naples"]
}

numCorrect = 0

for num , (question, answers) in enumerate(questions.items(), start=1):
    correctAnswer = answers[0]
    print(f"\nQuestion {num}: {question}")
    sortedAnswers = sorted(answers)
    labeledAnswers = dict(zip(ascii_lowercase, sortedAnswers))

    for label, answer in labeledAnswers.items():
        print(f"{label}. {answer}")  

    answerLabel = input("choice? ").lower() 
    answer = labeledAnswers.get(answerLabel)

    if answer == correctAnswer:
        print("correct")
        numCorrect += 1
    else:
        print(f"the asnwer is '{correctAnswer}', not {answer!r}")

print(f"\nYou got {numCorrect} out of {len(questions)} correct.")