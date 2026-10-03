class Solution:
    def encode(self, strs: List[str]) -> str:
        # Join list into a single string separated by a special char
        # Need a unique character to split by


        result = ""

        for word in strs:
            result += str(len(word)) + "#" + word

        return result

    def decode(self, s: str) -> List[str]:
        # Separate string into a list by a special char

        result, i, num = [], 0, ""

        while i < len(s):
            cur = s[i]


            if cur != '#':
                num += cur
                i += 1

            else:
                length = int(num)
                result.append(s[i + 1 : i + 1 + length])
                i += 1 + length
                num = ""

          
        return result
