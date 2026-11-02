class Solution:
    def isPalindrome(self, s: str) -> bool:
        # A left pointer at start and right pointer at end
        # If characters don't match we return false

        l,r = 0, len(s) - 1
        s = s.lower()

        # Ignore all non alphanumeric characters

        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            
            while l < r and not s[r].isalnum():
                r -= 1

            if s[l] != s[r]:
                return False
            l += 1
            r -= 1

        return True