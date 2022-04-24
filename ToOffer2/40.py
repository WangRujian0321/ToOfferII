# import heapq
# class Solution:
#     def getLeastNumbers(self, arr, k: int):
#         num = 0
#         heap = []
#         for item in arr:
#             if num < k:
#                 heapq.heappush(heap, -item)
#                 num += 1
#             elif num == k:
#                 heapq.heappush(heap, -item)
#                 heapq.heappop(heap)
#         return [-item for item in heap]

class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if k == len(arr):
            return arr
        p = arr[-1]
        i = 0
        for j in range(len(arr) - 1):
            if arr[j] <= p:
                arr[j], arr[i] = arr[i], arr[j]
                i += 1
        arr[i], arr[-1] = arr[-1], arr[i]
        n = len(arr)
        if k < i:
            return self.getLeastNumbers(arr[:i], k)
        elif k == i:
            return arr[:i]
        else:
            return arr[:i] + self.getLeastNumbers(arr[i:], k - i)


sol = Solution()
print(sol.getLeastNumbers([0,0,2,3,2,1,1,2,0,4], 10))

