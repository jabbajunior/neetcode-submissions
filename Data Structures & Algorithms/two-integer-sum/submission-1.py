class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = [target - num for num in nums]
        index = {}

        for i in range(len(nums)):
            if diff[i] in index.keys():
                return [index[diff[i]], i]

            index[nums[i]] = i
            