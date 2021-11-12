class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        
        # length of answer is length num1 + length num2
        # e.g. 99 * 99 = 9801, 99 * 9 = 891
        ans = [0] * (len(num1) + len(num2))
        
        # Do the step by step multiplication
        for i, v1 in enumerate(reversed(num1)):
            for j, v2 in enumerate(reversed(num2)):
                ans[i+j] += int(v1) * int(v2)
                ans[i+j+1] += ans[i+j] // 10           #carry
                ans[i+j] = ans[i+j] % 10
                
         
        # Remove leading 0's except 0 itself from backward
        while len(ans) > 1 and ans[-1] == 0:
            ans.pop()
            
        print(ans)
        return "".join(map(str, ans[::-1]))
