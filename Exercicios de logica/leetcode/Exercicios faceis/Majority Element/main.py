class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        filter = set(nums)
        maxn = 0
        num = 0
        for n in filter:
            r = nums.count(n)
            if r > maxn:
                maxn = r
                num = n
        return num
