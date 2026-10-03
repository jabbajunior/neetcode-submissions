class Solution:

    def encode(self, strs: List[str]) -> str:
        # Join list into a single string separated by a special char
        # Need a unique character to split by
        print()

        if strs == []:
            return str(None)

        return "中".join(strs)

    def decode(self, s: str) -> List[str]:
        # Separate string into a list by a special char
        #print("String is: ", s)

        if s == "None":
            #print("is none")
            return []

        return s.split("中")
