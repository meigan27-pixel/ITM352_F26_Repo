#interactive quiz system, version7
#make a dictionary with the questions and correct answers
#allow user to choose the option by its label
#improve usablility and look. keep track of correct answers
#randomize the order of the questions and the order of the answers
#refactor code to use functions

from string import ascii_lowercase
import random
import json

questionFile = open("questions.json", "r")
questions = json.load(questionFile)

NUM_QUESTIONS_PER_QUIZ = 5

def prepareQuestions(questions, numQuestions):
    numQuestions  = min(numQuestions, len(questions))
    return random.sample(list(questions.items()), k = numQuestions)

def getAnswer(question, alternatives):
    labeledAnswers = dict(zip(ascii_lowercase, alternatives))

    for label, answer in labeledAnswers.items():
        print(f"{label}. {answer}")

    while (answerLabel := input("choice? ").lower()) not in labeledAnswers:
        print(f"invalid choice. please select one of {', '.join(labeledAnswers.keys())}.")

    answer = labeledAnswers.get(answerLabel)
    return labeledAnswers[answerLabel]

def askQuestion(question, alternatives):
    correctAnswer = alternatives[0]
    orderedAlternatives = random.sample(alternatives, k = len(alternatives))
    answer = getAnswer(question, orderedAlternatives)
    if answer == correctAnswer:
        print("correct")
        return 1
    else:
        print(f"the answer is '{correctAnswer}', not {answer!r}")
        return 0
    
questions =  prepareQuestions(questions, NUM_QUESTIONS_PER_QUIZ)

numCorrect = 0

for num, (question, answers) in enumerate(questions, start = 1):
    print(f"\nQuestion {num}: {question}")
    numCorrect += askQuestion(question, answers)

print(f"\nYou got {numCorrect} correct.")