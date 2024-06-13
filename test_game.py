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

    def assert_proper_result(self, result, solved, strikes, balls):
        self.assertIsNotNone(result)
        self.assertEqual(solved, result.get_solved())
        self.assertEqual(strikes, result.get_strikes())
        self.assertEqual(balls, result.get_balls())

    def generate_question(self, question):
        self.game.question = question

    def test_exception_when_invalid_input(self):
        test_cases = [None, '12', '1234', '12s', '121']
        for tc in test_cases:
            with self.subTest(tc):
                self.assert_legal_argument(tc)

    def test_result_when_matched_input(self):
        self.generate_question('123')
        self.assert_proper_result(self.game.guess('123'), True, 3, 0)

    def test_result_when_unmatched_input(self):
        self.generate_question('123')
        self.assert_proper_result(self.game.guess('456'), False, 0, 0)

    def test_result_when_some_matched_input(self):
        self.generate_question('123')
        test_cases = [
            ('120', False, 2, 0),
            ('061', False, 0, 1),
            ('136', False, 1, 1),
        ]
        for tc in test_cases:
            with self.subTest(tc):
                self.assert_proper_result(self.game.guess(tc[0]), tc[1], tc[2], tc[3])
