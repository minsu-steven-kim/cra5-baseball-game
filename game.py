class Game:
    def __init__(self):
        self.question = ''

    def guess(self, number):
        self.assert_legal_value(number)
        if number == self.question:
            return GameResult(True, 3, 0)

    def assert_legal_value(self, number):
        if number is None:
            raise TypeError()
        if len(number) != 3:
            raise TypeError()
        for digit in number:
            if not ord('0') <= ord(digit) <= ord('9'):
                raise TypeError()
        if self.is_duplicated_digit(number):
            raise TypeError()

    def is_duplicated_digit(self, number):
        return number[0] == number[1] or number[1] == number[2] or number[2] == number[0]


class GameResult:
    def __init__(self, solved, strikes, balls):
        self.__solved = solved
        self.__strikes = strikes
        self.__balls = balls

    def get_solved(self):
        return self.__solved

    def get_strikes(self):
        return self.__strikes

    def get_balls(self):
        return self.__balls
