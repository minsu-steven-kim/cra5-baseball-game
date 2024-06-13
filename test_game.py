from unittest import TestCase

from game import Game


class TestGame(TestCase):
    def setUp(self):
        super().setUp()
        self.game = Game()

    def assert_illegal_argument(self, number):
        try:
            self.game.guess(number)
            self.fail()
        except TypeError:
            pass

    def test_exception_when_invalid_input(self):
        test_cases = [None, '12', '1234']
        for tc in test_cases:
            self.assert_illegal_argument(tc)
