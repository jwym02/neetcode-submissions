class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        unique_list = set()
        for num in nums:
            if num not in unique_list:
                unique_list.add(num)
            else:
                return num
