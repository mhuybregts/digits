import random


class Digits:
    """
    Digits represents an instance of the digits game. You can either save
    or match a digit, but you cannot do either twice in a row to the
    same digit. You score points by matching digits.
    """
    # The number of digits (0-9 in this case)
    NUMBER_DIGITS = 10

    # For determining the likelihood of showing an unsaved digit
    PROBABILITY_RANGE = 50
    PROBABILITY_FACTOR = 3

    def __init__(self) -> None:
        self.score = 0
        self.digits = [False] * self.NUMBER_DIGITS

    def __getmatch__(self) -> bool:
        val = random.randint(0, self.PROBABILITY_RANGE)
        return val > self.score * self.PROBABILITY_FACTOR

    def get_digit(self) -> int:
        """
        This function returns the next digit to be shown to
        the user. As the score of the user increases, it will
        be more likely to show a digit the user has not saved.
        """
        match = self.__getmatch__()
        if match and True in self.digits:
            new_digits = [num for num in range(len(self.digits))
                          if self.digits[num]]
            return random.choice(new_digits)

        return random.randint(0, self.NUMBER_DIGITS - 1)

    def save(self, digit: int) -> bool:
        """
        This function saves a digit. If the digit has already
        been saved, the function returns false, otherwise the
        function returns true.
        """
        if digit < 0 or digit > self.NUMBER_DIGITS:
            return False

        if not self.digits[digit]:
            self.digits[digit] = True
            return True

        return False

    def match(self, digit: int) -> bool:
        """
        This function matches a digit. If the digit has already
        been matched, the function returns false, othewrise the
        function returns true.
        """
        if digit < 0 or digit > self.NUMBER_DIGITS:
            return False

        if self.digits[digit]:
            self.score += 1
            self.digits[digit] = False
            return True

        return False
