#turn sentence from user input into a list of strings and reverse the list. put the list
#back into a string and print it out
#name: Meigan Mitsuyoshi
#Sept. 18, 2026

sentence = input("Enter a sentence: ")
wordList = sentence.split()
wordList.reverse()
reversed_sentence = " ".join(wordList)
print("Reversed sentence:", reversed_sentence)

joinedSentence = sentence + " " + reversed_sentence
print("Joined sentence:", joinedSentence)