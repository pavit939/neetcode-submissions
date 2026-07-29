class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        result = []
        for value in asteroids:
            while result and value < 0 and result[-1] > 0:
                if result[-1] < abs(value):
                    result.pop()
                elif result[-1] == abs(value):
                    result.pop()
                    break
                else:
                    break
            else:
                result.append(value)
        return result
                    






        