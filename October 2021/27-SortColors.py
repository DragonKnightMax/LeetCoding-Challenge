class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # start: red (0)
        # end: blue (2)
        start = 0
        end = len(nums) - 1
        
        # counter
        i = 0
        
        while i <= end:
            # Step 3: Swap 0 and 1
            if nums[i] == 0:
                nums[start], nums[i] = nums[i], nums[start]
                start += 1
                i += 1
            # Step 2: Leave 1's at front, proceed to next element
            elif nums[i] == 1:
                i += 1
            # Step 1: Place all 2's at the end
            else:
                nums[end], nums[i] = nums[i], nums[end]
                # Do not increment counter, check again the newly swapped nums[i]
                end -= 1
