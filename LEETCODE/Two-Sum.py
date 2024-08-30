class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} # val : index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return

"""
63 / 63 test cases passed.
Status: Accepted
Runtime: 59 ms
Memory Usage: 17.7 MB


You are here!
Your runtime beats 64.77 % of python3 submissions.


You are here!
Your memory usage beats 56.51 % of python3 submissions.
"""