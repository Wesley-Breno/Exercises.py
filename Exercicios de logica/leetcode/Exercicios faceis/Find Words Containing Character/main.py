class Solution:
    def findWordsContaining(self, words: list[str], x: str) -> list[int]:
        result = []
        for i in range(0, len(words)):
            if x in words[i]:
                result.append(i)
        return result     