class Solution:
    def maxProduct(self, n: int) -> int:
        n = [int(n) for n in str(n)]

        result = 0

        for i, n1 in enumerate(n):
            for i2, n2 in enumerate(n):
                if i == i2:
                    continue
                multi = n1 * n2
                if multi > result:
                    result = multi

        return result