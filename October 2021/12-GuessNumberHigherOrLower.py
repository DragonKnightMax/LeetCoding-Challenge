# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        # Binary Search
        low = 1
        high = n
        
        while low < high:
            # Use mid as guess
            mid = int((low + high) / 2)
            
            # guess == picked
            if guess(mid) == 0:
                return mid
            # guess < picked
            elif guess(mid) > 0:
                low = mid + 1
            # guess > picked
            else:
                high = mid - 1
                
        return low
