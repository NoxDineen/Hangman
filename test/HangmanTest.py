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

    def test_phrase_is_hidden(self):
        phrases = [
            {'plain': 'Hello World', 'hidden': '_____ _____'},
            {'plain': "It's got an apostrophe", 'hidden': "__'_ ___ __ __________"},
            {'plain': 'The number is 2 (two).', 'hidden': '___ ______ __ 2 (___).}'}
        ]
        for phrase in phrases:
            self.game.setPhrase(phrase.text)
            assert self.game.hiddenPhrase() == phrase.hidden

    def test_has_letter(self):
        self.game.setPhrase(self.phrase)
        guesses = [
            {'value':'e', 'expected': True},  # this is in the string Hello World
            {'value':'h', 'expected': True},  # this exists, but it's upper case, should return True anyway
            {'value':'x', 'expected': False},  # this isn't in the string
            {'value':123, 'expected': False},  # numbers wont exist in our phrase (digits will)
            {'value':(1, 2,), 'expected': False},  # what's this? a tuple or something
        ]
        for guess in guesses:
            assert self.game.hasLetter(guess.value) == guess.expected

    def test_make_guess(self):
        self.game.setPhrase(self.phrase)

        guess = 'e'
        result = self.game.makeGuess(guess)
        assert result == ['e']

        guess = 'x'
        result = self.game.makeGuess(guess)
        assert result == ['e', 'x']
