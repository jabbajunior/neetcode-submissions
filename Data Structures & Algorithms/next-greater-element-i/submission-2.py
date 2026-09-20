class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        '''
        Each element can have a next greater element
        It is in the next element
        '''

        output = [-1 for _ in range(len(nums1))]

        for i in range(len(nums1)):
            condition = False
            for j in range(len(nums2)):
                print("i_val: ", nums1[i], "j_val: ", nums2[j])

                if nums1[i] == nums2[j]:
                    print("EQUAL!")
                    condition = True

                if condition:
                    if nums2[j] > nums1[i]:
                        output[i] = nums2[j]
                        break
            print("NOT EQUAL!")

        return output
                