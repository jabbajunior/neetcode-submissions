class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev = {}

        for i in range(len(nums)):
            cur = nums[i]
            difference = target - cur

            if difference in prev:
                return [prev[difference], i]

            prev[cur] = i
            