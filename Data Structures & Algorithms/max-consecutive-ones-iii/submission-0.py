class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        '''
        Problem: 

        binary array nums
        return max num of consecutive 1's if you flip at most k 0's
        '''

        # Define window
        # Window is our current substring
        # We increase by flipping until we run out of flips, then we start unflipping from start
        # However can only flip indices that started as 0

        # Dont need to keep track of zeros since we can control that via the window itself

        num_flips = k
        longest = 0
        start = 0
        for end, value in enumerate(nums):
            if value == 0:
                if num_flips == 0:
                    while nums[start] == 1:
                        start += 1

                    # Skip first 0 and increment flips
                    start += 1
                    num_flips += 1

                num_flips -= 1

            longest = max(longest, end - start + 1)



        return longest