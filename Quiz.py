import Classes


def createQuiz():
    q0 = Classes.Questions('What is the 3rd day of the week? ', 'Tuesday', '')
    q1 = Classes.Questions('What is the name of Chris’s first dog? ', 'Benji', '')
    q2 = Classes.Questions('What street did we grow up on? ', 'Copperfield', '')
    q3 = Classes.Questions('Where did they serve $2 jager bombs on 6th? ', 'Latitude', '')
    listQuestions = [q0, q1, q2, q3]
    return listQuestions

def takeQuiz():
    listQuestions = createQuiz()
    i = 0
    score = 0
    while i < len(listQuestions):
        answer = input(listQuestions[i].question)
        listQuestions[i].setInput(answer)
        ##Alternate spaghetti code
        # listQuestions[i].setInput(input(listQuestions[i].question))
        ## Testing
        # print(listQuestions[i].checkAnswer())
        # print(listQuestions[i].uanswer)
        # print(listQuestions[i].canswer)
        if listQuestions[i].checkAnswer() == True:
            score = score + 1
        # print(listQuestions[i].uanwser)
        i = i + 1
    # print(listQuestions)
    print('Your total score is: ' + str(score))
    return listQuestions

def acceptQuiz():
    check = input('Do you want to take a quiz? Type "y"/"n" ').strip()
    if check[:1].lower() == 'y':
        takeQuiz()
    else:
        print('Bye!')
        quit()

def main():
    acceptQuiz()
    return
######################################################
main()