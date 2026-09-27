class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Have 2 variables, cur_count and cur_value. Sort nums before processing. When cur_value != what we are iterating, we see

        nums.sort()

        return nums[len(nums) // 2]
