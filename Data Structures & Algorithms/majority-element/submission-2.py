class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Return whichever element occurs the most (at least half of elements are majority)

        count = Counter(nums)
        return count.most_common()[0][0]

        # Is there a way to solve with O(n) time and O(1) space so not keeping track of anything past a single variable?