class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_map, t_map = defaultdict(int), defaultdict(int)

        for cs, ct in zip(s, t):
            s_map[cs] += 1
            t_map[ct] += 1
        
        return s_map==t_map