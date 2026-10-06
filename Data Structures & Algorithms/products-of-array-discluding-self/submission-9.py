class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Prefix/Suffix technique
        # Iterate from left to right and store prefix products for each indexin a prefix array, excluding the current index's number
        # Math prod has a default value of 1
        length = len(nums)

        prefix = [0] * length
        suffix = [0] * length

        res = [0] * length

        prefix[0] = nums[0]
        for i in range(1, length):
            prefix[i] = nums[i] * prefix[i-1]

        suffix[-1] = nums[-1]
        for i in range(length - 2, -1, -1):
            suffix[i] = nums[i] * suffix[i+1]

        # Algorithm is prefix before * suffix after
        res[0] = suffix[1]
        res[-1] = prefix[-2]

        for i in range(1, length - 1):
            res[i] = prefix[i - 1] * suffix[i + 1]
         
        #print("Nums: ", nums)
        #print("Prefix: ", prefix)
        #print("Postfix: ", suffix)

        return res