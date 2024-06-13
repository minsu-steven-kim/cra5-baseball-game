class Game:
    def __init__(self):
        self.question = ''

    def guess(self, number):
        self.assert_legal_value(number)
        return GameResult(True, 3, 0)

    def assert_legal_value(self, number):
        if number is None:
            raise TypeError()
        if len(number) != 3:
            raise TypeError()
        for digit in number:
            if not ord('0') <= ord(digit) <= ord('9'):
                raise TypeError()
        if self.isDuplicatedDigit(number):
            raise TypeError()

    def isDuplicatedDigit(self, number):
        return number[0] == number[1] or number[1] == number[2] or number[2] == number[0]


class GameResult:
    def __init__(self, solved, strikes, balls):
        self.solved = solved
        self.strikes = strikes
        self.balls = balls

