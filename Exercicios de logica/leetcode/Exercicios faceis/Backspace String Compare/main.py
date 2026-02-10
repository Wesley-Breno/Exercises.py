class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def build(s):
            stack = []
            for c in s:
                if c == '#':
                    if stack:
                        stack.pop()
                else:
                    stack.append(c)
            return stack

        return build(s) == build(t)