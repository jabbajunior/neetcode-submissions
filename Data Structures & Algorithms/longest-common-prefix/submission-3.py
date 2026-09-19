class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]

        shortest = min(strs, key=len)
        common_prefix = shortest

        # Loop through every string except first
        for item in strs[1:]:
            # item = neet
            # strs[1] = code
            # need to loop through smallest
            for i in range(len(common_prefix)):
                # If we don't match, trim the rest of common_prefix
                if item[i] != common_prefix[i]:
                    common_prefix = common_prefix[:i]
                    break

        return common_prefix
        