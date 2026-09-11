class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Early return condition
        # O(1)
        s_len = len(s)

        if s_len != len(t):
            return False

        # Its being returned here as a LIST
        s_sorted = sorted(s)
        t_sorted = sorted(t)

        return s_sorted == t_sorted