class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        unique_counter = {}
        for num in nums:
            if num in unique_counter:
                unique_counter[num] += 1
            else: # initialize counter
                unique_counter[num] = 1
        
        count_list = [(count, num) for (num, count) in unique_counter.items()]
        count_list.sort(reverse=True)

        return_list = []
        for i in range(k):
            return_list.append(count_list[i][1])
        return return_list