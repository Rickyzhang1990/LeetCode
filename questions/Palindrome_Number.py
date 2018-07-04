class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        index = [str(x).find(i) for i in str(x)]
        index_v = index[::-1] 
        return index == index_v 
