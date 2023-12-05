import random
import time


class TypingQuiz:
    def __init__(self, startTime=None, testTime=30, charsTotal=0, charsCorrect=0):
        """Initialize TypingQuiz object.

        Parameters:
        - startTime (float): The start time of the quiz, default is None.
        - testTime (int): The duration of the typing test in seconds, default is 30 seconds.
        - charsTotal (int): Total number of characters typed by the user, default is 0.
        - charsCorrect (int): Number of correctly typed characters, default is 0.
        """
        if startTime is None:
            startTime = time.time()
        self.elapsedTime = time.time() - startTime
        self.testTime = testTime
        self.charsTotal = charsTotal
        self.charsCorrect = charsCorrect

    def startUpMenu(self):
        """Display the welcome message and get the difficulty level from the user.

        Returns:
        - int: Difficulty level chosen by the user (1 for Easy, 2 for Medium, 3 for Hard).
        """
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
        """Run the typing test based on user input and display the results."""
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
        accuracy = str(round(self.charsCorrect / self.charsTotal, 4) * 100) + "%"
        wordsPerMinute = round((self.charsTotal / 5) / (self.elapsedTime / 60), 2)
        print(self.elapsedTime)
        print(f"You typed {wordsPerMinute} words per minute with {accuracy} accuracy!")
        if input("\nWould you like to play again?\nType 1 to play again\nType 2 to exit\n") == str(1):
            self.charsTotal = 0
            self.charsCorrect = 0
            self.runTest()

    def printPassage(self, testFilePath):
        """Display the passage for the typing test and record user input.

        Parameters:
        - testFilePath (str): File path to the text passage for the typing test.
        """
        startTime = time.time()
        self.elapsedTime = time.time() - startTime
        with open(testFilePath, 'r') as file:
            for line in file:
                userLetterIndex = 0
                self.elapsedTime = time.time() - startTime
                if self.elapsedTime >= self.testTime:
                    return
                print(line)
                usersLine = input()
                for char in line:
                    if userLetterIndex < len(usersLine):
                        if char == usersLine[userLetterIndex]:
                            self.charsCorrect += 1
                        userLetterIndex += 1
                        self.charsTotal += 1


# Instantiate the TypingQuiz class
TypingQuizInstance = TypingQuiz()

# Run the typing test
TypingQuizInstance.runTest()
