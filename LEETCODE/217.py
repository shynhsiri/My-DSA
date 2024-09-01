class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False

"""
Accepted

Runtime
419
ms
Beats
55.69%

Memory
31.92
MB
Beats
48.82%
"""