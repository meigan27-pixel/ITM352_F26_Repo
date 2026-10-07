#interactive quiz system, version6
#make a dictionary with the questions and correct answers
#allow user to choose the option by its label
#improve usablility and look. keep track of correct answers
#randomize the order of the questions and the order of the answers

from string import ascii_lowercase
import random

questions = {
    "what is the capital of france?": ["Paris", "Toulouse", "Lyon"],
    "what is the capital of germany?": ["Berlin", "Hamburg", "Munich"],
    "what is the capital of italy?": ["Rome", "Milan", "Naples"]
}

NUM_QUESTIONS_PER_QUIZ = 5
numQuestions = min(NUM_QUESTIONS_PER_QUIZ, len(questions))
selectedQuestions = random.sample(list(questions.items()), numQuestions)
numCorrect = 0

for num , (question, answers) in enumerate(questions.items(), start=1):
    correctAnswer = answers[0]
    print(f"\nQuestion {num}: {question}")
    sortedAnswers = sorted(answers)
    labeledAnswers = dict(zip(ascii_lowercase, random.sample(sortedAnswers, k=len(sortedAnswers))))

    for label, answer in labeledAnswers.items():
        print(f"{label}. {answer}")

    while (answerLabel := input("choice? ").lower()) not in labeledAnswers:
        print(f"invalid choice. please select one of {", ".join(labeledAnswers.keys())}.")

    #answerLabel = input("choice? ").lower() 
    answer = labeledAnswers.get(answerLabel)

    if answer == correctAnswer:
        print("correct")
        numCorrect += 1
    else:
        print(f"the asnwer is '{correctAnswer}', not {answer!r}")

print(f"\nYou got {numCorrect} out of {len(questions)} correct.")