class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        # sum(low, mid, high) = 0
        
        # Sort the nums in ascending order
        results = []
        
        nums.sort()
        length = len(nums)
        
        # At least 3 numbers
        for low in range(length-2):
            
            # Ensure there is negative number
            if nums[low] > 0:
                break
                
            # Skip duplicates after 1st triplet found
            if low > 0 and nums[low] == nums[low-1]:
                continue
                
            mid = low + 1
            high = length - 1
            
            while mid < high:
                three_sum = nums[low] + nums[mid] + nums[high]
                
                # Shift mid pointer to right to get larger num
                if three_sum < 0:
                    mid += 1
                    
                    # Ensure shift to larger number
                    while mid < high and nums[mid] == nums[mid-1]:
                        mid += 1
                
                # Shift right pointer to left to get smaller num
                elif three_sum > 0:
                    high -= 1
                    
                    # Ensure shift to smaller number
                    while mid < high and nums[high] == nums[high+1]:
                        high -= 1
                
                # Triplet found
                else:
                    results.append([nums[low], nums[mid], nums[high]])
                    mid += 1
                    high -= 1
                    
                    # Check again
                    while mid < high and nums[mid] == nums[mid-1]:
                        mid += 1
                    while mid < high and nums[high] == nums[high+1]:
                        high -= 1
                        
        return results
