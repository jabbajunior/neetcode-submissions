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

        result, i = [], 0

        while i < len(s):
            j = i

            while s[j] != '#':
                j += 1
                
            length = int(s[i:j])
            result.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length

        #print(result)
        return result
