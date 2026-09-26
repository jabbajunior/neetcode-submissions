class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # move all values matching val to end of nums array
        # return k so that it matches all non val values

        length = len(nums)

        # Edge Cases
        if length == 0:
            return 0

        elif length == 1:
            if nums[0] == val:
                return 0
            else:
                return 1
        
        start = 0
        count = 0

        for i in range(length):
            # Every non val we move to front
            if nums[i] != val:
                nums[start] = nums[i]
                start += 1
                count += 1


        return count

        
        # pUT BAD VALUES AT THE END
        

