from unittest import TestCase

from game import Game, GameResult


class TestGame(TestCase):
    def setUp(self):
        super().setUp()
        self.game = Game()

    def assert_legal_argument(self, number):
        try:
            self.game.guess(number)
            self.fail()
        except TypeError:
            pass

    def test_exception_when_invalid_input(self):
        test_cases = [None, '12', '1234', '12s', '121']
        for tc in test_cases:
            with self.subTest(tc):
                self.assert_legal_argument(tc)

    def test_result_when_matched_input(self):
        self.game.question = '123'
        result: GameResult = self.game.guess('123')

        self.assertIsNotNone(result)
        self.assertTrue(result.get_solved())
        self.assertEqual(3, result.get_strikes())
        self.assertEqual(0, result.get_balls())
