class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        firstReturn = -1
        lastReturn = -1

        def first(start, end):
            if start > end:
                return -1
            mid = (start + end) // 2
            if nums[mid] == target:
                # found a match; check if it's the first occurrence
                if mid == 0 or nums[mid - 1] < target:
                    return mid
                return first(start, mid - 1)
            elif nums[mid] < target:
                return first(mid + 1, end)
            else:
                return first(start, mid - 1)

        def last(start, end):
            if start > end:
                return -1
            mid = (start + end) // 2
            if nums[mid] == target:
                # found a match; check if it's the last occurrence
                if mid == len(nums) - 1 or nums[mid + 1] > target:
                    return mid
                return last(mid + 1, end)
            elif nums[mid] > target:
                return last(start, mid - 1)
            else:
                return last(mid + 1, end)

        firstReturn = first(0, len(nums) - 1)
        lastReturn = last(0, len(nums) - 1)
        ans = [firstReturn, lastReturn]
        return ans