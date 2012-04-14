from Hangman import Hangman


class TestHangman:
    def __init__(self):
        self.game = Hangman()
        self.phrase = "Hello World"

    def test_hangman_init(self):
        isinstance(self.game, Hangman)

    def test_accepts_a_phrase(self):
        self.game.setPhrase(self.phrase)

        assert self.game.realPhrase() == self.phrase
