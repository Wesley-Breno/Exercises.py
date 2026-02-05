class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        cont = 0
        for n in nums:
            if n < k:
                cont += 1
        return cont
