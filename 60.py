from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnts = Counter(nums)
        lst = heapq.nlargest(k,[(v,k) for k,v in cnts.items()])
        return [x[1] for x in lst]