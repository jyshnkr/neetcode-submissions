class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_map, t_map = defaultdict(int), defaultdict(int)

        for ch in s:
            s_map[ch] += 1
        
        for ch in t:
            t_map[ch] += 1

        return s_map==t_map