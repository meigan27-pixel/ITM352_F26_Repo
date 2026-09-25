emotions = ["surprise", "sad", "fear", "happy"]

isItTrue = emotions[-1] == "happy" and len(emotions) > 3
print(isItTrue)
#print(emotions[3] == "happy" and len(emotions) > 3)
if emotions[-1] == "happy" and len(emotions) > 3:
    print("true")
else:
    print("false")