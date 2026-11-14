class Solution:
    def isValid(self, s: str) -> bool:
        # use a stack 
        # only push lft
        # pul right
        # if popping when empty, return false
        legend = {'(': ')', '{':'}', '[':']'}
        seen = list()

        for char in s:
            # Left
            if char in legend:
                seen.append(char)
            else:
                if len(seen) == 0:
                    return False
                if legend[seen[-1]] == char:
                    seen.pop()
                else:
                    return False

        if len(seen) > 0:
            return False

        return True
