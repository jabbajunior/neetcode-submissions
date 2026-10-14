class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        We convert nums into a list
        At each element we determine if this is the start of a sequence by looking up if num-1 exists in set
            If it does, we have a sequence
                Check +1 until no more exist and return the largest one
        """

        max_seq = 0

        lookup = set(nums)

        for num in nums:
            if num-1 not in lookup:
                seq = 0
                
                for i in range(100000):
                    if num + i in lookup:
                        seq += 1
                    else:
                        break

                if seq > max_seq:
                    max_seq = seq

        
        return max_seq
        """
        Needs to run in O(n) time
        No sorting allowed
        """

        """
        Can do 2 passes
        First finds smallest element
        Next finds all consecutive elements
        
        Only issue is smallest element is not guaranteed to have a consecutive sequence
        """