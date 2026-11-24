class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 1. create a set to remove dupes
        # 2. look for startings of sequences (num -1 not in set)
        # 3. form the sequence by searching for num + 1 in the set, increase counter per find
        # 4. if counter == len(set), stop the search
        # 5. return the longest list, that is the longest sequence
        # 6. return longest streak


        # 1. create a set to remove dupes, and a list to store all the sequences
        nums_set = set(nums)
        list_of_sequences = []
        longest = 0

        # 2. look for startings of sequences (num -1 not in set)
        for num in nums_set:
            if num - 1 not in nums_set:
                current_num = num
                streak = 1
                while current_num + 1 in nums_set:
                    current_num += 1
                    streak += 1
                longest = max(longest, streak)

        return longest