class Solution:
    def arrangeCoins(self, n: int) -> int:
        # Using formula
        # s = (n/2)(2a + (n-1)d)
        # a = 1, d = 1
        # n^2 + n - 2s = 0
        # n = (1/2)(-1 + sqrt(1+8s))
        
        return int((-1 + sqrt(1 + (8 * n))) / 2)
