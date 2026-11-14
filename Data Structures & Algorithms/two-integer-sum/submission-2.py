class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # We make a difference array
        diff = [target - num for num in nums]
        seen = {}

        for i, num in enumerate(nums):
            if diff[i] not in seen:
                seen[num] = i
            else:
                return [seen[diff[i]], i]

        return []