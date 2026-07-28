from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = defaultdict(int)
        freq = [[] for i in range(len(nums)+1)]
        for num in nums:
            hash_map[num] += 1
        for key, value in hash_map.items():
            freq[value].append(key)
        res = []
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res


        