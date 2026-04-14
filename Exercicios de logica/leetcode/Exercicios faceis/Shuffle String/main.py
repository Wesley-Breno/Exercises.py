class Solution:
    def restoreString(self, s: str, indices: list[int]) -> str:
        new_s = [[] for _ in range(0, len(s))]

        for i, e in enumerate(indices):
            new_s[e].append(s[i])

        result = ''
        for c in new_s:
            result += c[0]
        return result