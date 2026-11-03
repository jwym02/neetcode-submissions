class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix & suffix
        # prefix: [1,2,4,6] -> [1, 1, 2, 8]
        # suffix: [1,2,4,6] -> [48, 24, 6, 1]
        n = len(nums)
        

        # prefix
        prefix = [0] * n
        prefix[0] = 1
        for i in range(1, n):
            prefix[i] = prefix[i-1] * nums[i-1]

        # suffix
        suffix = [0] * n
        suffix[-1] = 1
        for i in range(n-2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i+1]
            
        # result
        result = [0] * n
        for i in range(n):
            result[i] = prefix[i] * suffix[i]

        return result