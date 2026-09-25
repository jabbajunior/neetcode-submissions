class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        '''
        i < j, good pair if num[i] == num[j]
        '''

        count = 0

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    count += 1

        return count
        