class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        def get_pos(num):
            if num in arr2:
                return arr2.index(num)
            else:
                return len(arr2) + num
        return sorted(arr1, key=get_pos)