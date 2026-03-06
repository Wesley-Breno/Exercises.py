class Solution:
    def average(self, salary: list[int]) -> float:
        up = max(salary)
        down = min(salary)

        salary.remove(up)
        salary.remove(down)

        return sum(salary) / len(salary)