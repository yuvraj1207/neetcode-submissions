
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        for num, freq in Counter(nums).most_common(k):
            result.append(num)
        return result