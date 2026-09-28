class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        res = []

        i = 0
        for key, value in count.most_common():
            if i >= k:
                break

            res.append(key)
            i += 1

        return res