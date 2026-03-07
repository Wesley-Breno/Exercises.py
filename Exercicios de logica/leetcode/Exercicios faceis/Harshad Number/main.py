class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        x_string = str(x)

        soma = 0
        for d in x_string:
            soma += int(d)

        return soma if x % soma == 0 else -1