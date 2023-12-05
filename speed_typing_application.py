import random
import time


class TypingQuiz:
    def __init__(self, startTime=None, testTime=15, wordsTotal=0, wordsCorrect=0):
        if startTime is None:
            startTime = time.time()
        self.elapsedTime = time.time() - startTime
        self.testTime = testTime
        self.wordsTotal = wordsTotal
        self.wordsCorrect = wordsCorrect

    def startUpMenu(self):
        print("Welcome to the Speed Typing Test!")
        while True:
            try:
                difficulty = input("Enter test difficulty\nType 1 for Easy\nType 2 for Medium\nType 3 for Hard: ")
                number = int(difficulty)

                if 1 <= number <= 3:
                    return number
                else:
                    raise ValueError("Input must be between 1 and 3.")
            except ValueError as ve:
                print("Invalid input. Please enter a valid integer.\n", ve)

    def runTest(self):
        difficulty = self.startUpMenu()
        randomTestNumber = random.randint(1, 5)
        if difficulty == 1:
            print("\nYou've chosen an easy test.\n")
            testFilePath = "easy_typing_templates/easy_template" + str(randomTestNumber)
        elif difficulty == 2:
            print("\nYou've chosen a medium test.\n")
            testFilePath = "medium_typing_templates/medium_template" + str(randomTestNumber)
        else:
            print("\nYou've chosen a hard test.\n")
            testFilePath = "hard_typing_templates/hard_template" + str(randomTestNumber)
        seconds = 3
        while seconds > 0:
            print(f"Your test will start in {seconds} seconds")
            time.sleep(1)
            seconds -= 1
        print("\nTest started!\n")

        self.printPassage(testFilePath)
        wordsPerMinute = round(self.wordsCorrect / self.testTime, 2) * 60

        print(wordsPerMinute)
        print(self.wordsTotal)
        print(self.elapsedTime)

        print(f"You typed {wordsPerMinute} words per minute!")

    def printPassage(self, testFilePath):
        startTime = time.time()
        self.elapsedTime = time.time() - startTime
        with open(testFilePath, 'r') as file:
            for line in file:
                userWordIndex = 0
                self.elapsedTime = time.time() - startTime
                if self.elapsedTime >= self.testTime:
                    return
                print(line)
                usersLine = input().split()
                for word in line.split():
                    if userWordIndex < len(usersLine) and word == usersLine[userWordIndex]:
                        self.wordsCorrect += 1
                    userWordIndex += 1
                    self.wordsTotal += 1


TypingQuizInstance = TypingQuiz()

TypingQuizInstance.runTest()
