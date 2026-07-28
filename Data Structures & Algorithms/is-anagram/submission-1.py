from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashMapS = defaultdict(int)
        hashMapT = defaultdict(int)
        for i in range(len(s)):
            hashMapS[s[i]] += 1
            hashMapT[t[i]] += 1
        return hashMapS == hashMapT

        