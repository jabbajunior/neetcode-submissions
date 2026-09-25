class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # Intuition
        # If we get the count of 1s and then do math to it we can determine it

        count = Counter(nums)
        res = 0

        return int(sum([(v * (v - 1)) // 2 for k, v in count.items()]))
        