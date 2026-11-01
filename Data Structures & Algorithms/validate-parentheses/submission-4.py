class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}

        for char in s:
            # Is a right parenthesis
            if char in mapping:
                if len(stack) == 0:
                    return False
                if mapping[char] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        return not bool(stack)

        
        
