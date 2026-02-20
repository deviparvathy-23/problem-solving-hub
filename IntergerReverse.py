#Problem
"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
 

Constraints:

-2^31 <= x <= 2^31 - 1
"""

#Solution
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        if x<0:
            s=str(x)
            p="-"+s[:0:-1]
            n=int(p)
            if n<math.pow(-2,31):
                return 0
            else:
                return n 
            
        else:
            s=str(x)
            n=int(s[::-1])
            if n>math.pow(2,31)-1:
                return 0
            else:
                return n 
