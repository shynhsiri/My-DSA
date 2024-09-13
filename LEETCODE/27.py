class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        n = len(nums)

        while i < n:
            if nums[i] == val:
                nums[i] = nums[n-1]
                n -= 1
            else:
                i += 1

        return n


"""
Accepted

Runtime
44
ms
Beats
11.29%

Memory
16.54
MB
Beats
22.79%
"""