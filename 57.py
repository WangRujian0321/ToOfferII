class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:

        def get_bucket_id(num, bucket_size):
            if num < 0:
                ans = ((num + 1) // bucket_size) - 1
            else:
                ans = num // bucket_size
            return ans

        bucket_map = {}
        for i, num in enumerate(nums):
            bucket_id = get_bucket_id(num, t + 1)

            if bucket_id in bucket_map:
                return True
            elif bucket_id - 1 in bucket_map and abs(num - bucket_map[bucket_id - 1]) <= t:
                return True
            elif bucket_id + 1 in bucket_map and abs(num - bucket_map[bucket_id + 1]) <= t:
                return True

            bucket_map[bucket_id] = num

            if i - k >= 0:
                del_id = get_bucket_id(nums[i - k], t + 1)
                bucket_map.pop(del_id)

        return False