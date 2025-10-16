class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for e in s:
            if e in t:
                t = t.replace(e, '', 1)
        return t
