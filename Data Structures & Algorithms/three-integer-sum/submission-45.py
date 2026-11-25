class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 0. sort the nums list first
        # 1. set left, middle and right boundary
        # 2. always move middle boundary down to (left + 1) first
        # 3. if left + middle + right > 0, move right down by 1
        # 4. if sum of 0 achieved, move left + 1, restart the cycle

        # 0. sort the nums list
        nums.sort()
        result = []
        i = 0
        
        # 1. set pointers
        while i < len(nums) - 2:
            left, right = i + 1, len(nums) - 1
            if i > 0 and nums[i] == nums[i-1]: # skip duplicates
                i += 1
                continue
            
            while left < right:
                sum = nums[i] + nums[left] + nums[right] # -4 + -1 + 2 = -3
                if sum < 0:
                    left += 1
                elif sum > 0: 
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    # skip duplicates again for left
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
            i += 1
        return result