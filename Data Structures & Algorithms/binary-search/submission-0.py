class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # unique numberrs
        # ascending order
        # Binary search

        lo, hi = 0, len(nums) - 1

        while lo <= hi:
            index = (lo + hi) // 2

            if nums[index] == target:
                return index

            elif nums[index] < target:
                lo = index + 1

            else:
                hi = index - 1

        return -1
        