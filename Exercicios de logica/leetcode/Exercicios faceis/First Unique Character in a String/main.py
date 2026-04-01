class Solution:
    def firstUniqChar(self, s: str) -> int:
        origin = s

        while len(s) > 0:
            char = s[0]
            qtd = s.count(char)
            if qtd == 1:
                return origin.index(char)
            s = s.replace(char, '')

        return -1