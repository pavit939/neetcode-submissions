class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scores = []
        for i in operations:
            if i not in ["+", "C", "D"]:
                scores.append(int(i))
            elif i == "+":
                scores.append(sum(scores[-2:]))
            elif i == "C":
                scores.pop()
            else:
                scores.append(scores[-1] * 2)
        return sum(scores)

        