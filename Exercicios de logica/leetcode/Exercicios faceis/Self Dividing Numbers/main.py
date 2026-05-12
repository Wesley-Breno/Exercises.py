class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> list[int]:
        def check_divisible(num):
            if "0" in str(num):
                return False
            for n in str(num):
                if num % int(n) != 0:
                    return False
            return True

        result = []
        for i in range(left, right + 1):
            if check_divisible(i):
                result.append(i)
        return result