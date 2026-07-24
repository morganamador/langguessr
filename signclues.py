class SignClue:

    def __init__(self, clue: str, region: str):
        self.clue = clue
        self.region = region
    def cluematch(self, text: str):
        if self.clue in text:
            return True
        else:
            return False
