class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        numbers = set(nums)
        longest = 0

        for num in numbers:
            # start of sequence
            if num - 1 not in numbers:
                count = 1

                while num + count in numbers:
                    count += 1

                longest = max(longest, count)

        return longest