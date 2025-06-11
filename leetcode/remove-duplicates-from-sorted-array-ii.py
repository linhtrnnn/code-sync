class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k = 0
        twice = False

        for i in range(1, len(nums), 1):
            if nums[i] > nums[k]:
                twice = False
                k += 1
                nums[k] = nums[i]
                continue 

            elif twice is False and nums[i] == nums[k]:
                twice = True
                k += 1
                nums[k] = nums[i]
                continue

        return k + 1