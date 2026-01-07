class WordFilter:
    def __init__(self, words: list[str]):
        self.lookup = {}

        for index, word in enumerate(words):
            n = len(word)
            for i in range(1, n + 1):
                prefix = word[:i]
                for j in range(n):
                    suffix = word[j:]
                    self.lookup[prefix + "#" + suffix] = index

    def f(self, pref: str, suff: str) -> int:
        return self.lookup.get(pref + "#" + suff, -1)
