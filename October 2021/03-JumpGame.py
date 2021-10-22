class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # possible index that can be reached
        possible = 0
        last = len(nums)
        
        # Check each index one by one
        for i in range(last):
            
            # Stop when current index exceeds possible
            if i > possible:
                return False
            
            # Jump with max length and update if larger
            next_i = i + nums[i]
            if next_i > possible:
                possible = next_i
                
        return True
