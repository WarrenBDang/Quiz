class Questions:

    def __init__(self, question, correct, input):
        self.question = question
        self.canswer = correct.lower()
        self.uanswer = input.lower()


    def setInput(self, input):
        self.uanswer = input
        return self


    def checkAnswer(self):
        bool = False
        if self.uanswer == self.canswer:
            bool = True
        return bool


# test = Questions("What is this?", "I Don't know")
