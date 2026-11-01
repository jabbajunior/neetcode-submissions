class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        left = ["(", "{", "["]
        right = [")", "}", "]"]

        for char in s:
            if char in left:
                stack.append(char)

            elif char in right:
                if not bool(stack):
                    print("")
                    return False

                if stack[-1] == "(" and char == ")":
                    stack.pop()
                    continue
                elif stack[-1] == "{" and char == "}":
                    stack.pop()
                    continue
                elif stack[-1] == "[" and char == "]":
                    stack.pop()
                    continue
                else:
                    return False

        return not bool(stack)
                    

        # Operations LIFO
        # append add to end
        # pop remove from start
        # peek look at start


        # Input is ({[]})

        # Fails if input is {[}]
        