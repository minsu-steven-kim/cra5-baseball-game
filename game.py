class Game:
    def guess(self, number):
        if number is None:
            raise TypeError()

        if len(number) != 3:
            raise TypeError()

        for digit in number:
            if not ord('0') <= ord(digit) <= ord('9'):
                raise TypeError()

        if number[0] == number[1] or number[1] == number[2] or number[2] == number[0]:
            raise TypeError()
