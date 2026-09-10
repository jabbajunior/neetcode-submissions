class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        '''
        Make a frequency list of the same size and if we increment past 1 we return early
        '''
        freq = set()

        for val in nums:

            if val in freq:
                return True

            freq.add(val)

        return False