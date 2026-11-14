class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        max_len = 0
        seen = set()

        for end in range(len(s)):
            # Shrink window until we can add s[end]
            while s[end] in seen:
                seen.remove(s[start])
                start += 1

            # Now our window is correctly sized
            seen.add(s[end])

            max_len = max(max_len, end - start + 1)

        return max_len
       
            


