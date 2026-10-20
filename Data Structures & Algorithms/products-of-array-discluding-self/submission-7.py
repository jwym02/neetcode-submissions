class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # product of left side (prefix) & product of right side (suffix)
        # nums: [1, 2, 4, 6]
        # prefix: [1, 2, 4, 6] -> [1, 1, 2, 8]

        n = len(nums)
        prefix = [0] * n
        prefix[0] = 1 # [1, 0, 0, 0]
        for i in range(1, n):
            prefix[i] = nums[i-1] * prefix[i-1] 
            # i=1, prefix[1]=1, i=2, prefix[2]=2, i=3, prefix[3]=8

        # nums: [1, 2, 4, 6]
        # suffix: [1, 2, 4, 6] -> [48, 24, 6, 1]
        suffix = [0] * n # [0, 0, 0, 1]
        suffix[n-1] = 1
        for i in range(n-2, -1, -1):
            suffix[i] = nums[i+1] * suffix[i+1]

        result = [0] * n
        for i in range(n):
            result[i] = prefix[i] * suffix[i]

        return result
