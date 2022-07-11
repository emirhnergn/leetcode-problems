class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sn = ''
        mx = 0
        for c in s:
            if c not in sn:
                sn+=c
            else:
                sn = sn[sn.index(c) + 1:] + c
            mx = max(mx, len(sn))
        return mx
            
            