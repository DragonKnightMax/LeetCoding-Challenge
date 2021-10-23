class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # Hashing to detect duplicates
        
        # n = length of nums
        # elements: [1, n]
        # index: 0 to n-1
        
        duplicates = []
        
        for x in nums:
            # Record the occurrence of n with array indexing
            i = abs(x) - 1
            
            # if positive at nums[i], make it negative
            if nums[i] > 0:
                nums[i] *= -1
            else:
                # Restore from hashing to original value
                duplicates.append(abs(x))
          
        return duplicates
