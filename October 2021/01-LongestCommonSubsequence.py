class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Dynamic Programming
        
        # Fill up the table with 0's
        dp = [[0 for j in range(len(text2))] for i in range(len(text1))]

        # Compare
        for i in range(len(text1)):
            for j in range(len(text2)):
            
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + (dp[i-1][j-1] if (i and j > 0) else 0)
                
                else:
                    x = dp[i-1][j] if (i > 0) else 0
                    y = dp[i][j-1] if (j > 0) else 0
                    dp[i][j] = max(x, y)
                    
        return dp[-1][-1]
      
      # Lookup Table
      #    a c e
      #  a 1 1 1
      #  b 1 1 1
      #  c 1 2 2
      #  d 1 2 2
      #  e 1 2 3
