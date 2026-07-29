class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [] #temp, index
        output = [0] * len(temperatures)
        for index, temp in enumerate(temperatures):
            while result and temp > result[-1][0]:
                resultTemp , resultIndex = result.pop()
                output[resultIndex] = index - resultIndex
            result.append((temp, index))
        return output


        