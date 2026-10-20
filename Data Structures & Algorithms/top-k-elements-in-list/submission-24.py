class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create a hash, go through nums and create counter for each num
        # return the highest number by converting dict into a list, sort list
        num_count = {}
        for num in nums:
            if num not in num_count:
                num_count[num] = 1
            else:
                num_count[num] += 1
        
        # now i need to create a list & reverse it, return the first k
        count_list = [(count, num) for num, count in num_count.items()]
        count_list.sort(reverse=True)
        return [num for count,num in count_list[:k]]