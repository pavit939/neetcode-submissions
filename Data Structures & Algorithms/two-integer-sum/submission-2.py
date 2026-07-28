from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = defaultdict(int)
        for i in range(len(nums)):
            res = target - nums[i]
            if res in hash_map:
                return [hash_map[res], i]
            hash_map[nums[i]] = i
         
        