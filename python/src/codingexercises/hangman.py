class Hangman:
    def __init__(self, word):
        self.guesses = set()
        self.word = word
        self.maskedWord = "_"*len(word)
        self.nBodyParts = 0
        self.maxBodyParts = 6
        self.status = "ongoing"

    def guess(self, char):
        if self.status != "ongoing":
            raise ValueError("The game has already ended.")
        if char in self.guesses:
            raise ValueError("You already guessed this letter.")
        if char in self.word:
            self.maskedWord = ''.join([c if c in self.guesses else (char if c == char else '_') for c in self.word])
            if self.maskedWord == self.word:
                self.status = "win"
        else:
            self.nBodyParts += 1
            if self.nBodyParts == self.maxBodyParts:
                self.status = "lose"
        self.guesses.add(char)

    def getMaskedWord(self):
        return self.maskedWord

    def getStatus(self):
        return self.status

    def getPartsHanging(self):
        if 0 == self.nBodyParts:
            return "None"
        if 1 == self.nBodyParts:
            return "Head"
        if 2 == self.nBodyParts:
            return "Head and torso"
        if 3 == self.nBodyParts:
            return "Head, torso and left leg"
        if 4 == self.nBodyParts:
            return "Head, torso and both legs"
        if 5 == self.nBodyParts:
            return "Head, torso, left arm and both legs"
        if 6 == self.nBodyParts:
            return "Head, torso, both arms and both legs. You're dead!"
