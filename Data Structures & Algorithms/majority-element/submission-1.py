class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Return whichever element occurs the most (at least half of elements are majority)

        count = Counter(nums)
        return count.most_common()[0][0]