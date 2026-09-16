#try to append tuple. it wont work
#Name: Meigan Mitsuyoshi
#Sept. 16, 2026

surveyRespondents = (1012, 1035, 1021, 1053)
#surveyRespondents.append(1054) attribute error

surveyRespondents = surveyRespondents + (1054,)
print("updated survey respondents:", surveyRespondents)