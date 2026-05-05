from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom = Counter(ransomNote)
        ransomRange = ransom.copy()
        mag = Counter(magazine)

        for key, value in ransomRange.items():
            if mag[key] >= value:
                ransom.pop(key)

        if ransom == {}:
            return True
        return False