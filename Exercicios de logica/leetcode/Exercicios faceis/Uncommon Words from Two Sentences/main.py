class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> list[str]:
        all_setences = str(s1 + " " + s2).split(" ")
        result = []

        for word in all_setences:
            if all_setences.count(word) > 1:
                continue
            result.append(word)

        return result