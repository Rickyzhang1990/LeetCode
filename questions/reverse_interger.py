class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
      
        if x >= 0:
            b = int("".join(list(str(x))[::-1]))
        else:
            b = int("-" + "".join(list(str(x).lstrip("-"))[::-1]))
        if  abs(b) < 2**31:   return b 
        else:   return 0
