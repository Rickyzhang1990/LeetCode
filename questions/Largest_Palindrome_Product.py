class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}
        count = 0
        for x in s:
            if x in dic:
                dic[x] += 1
            else:
                dic[x] =1 
        for i in dic:
            if dic[i] %2 != 0 :
                count += 1
        if len(dic) >1 and count != 0:
            length = len(s) - count + 1
        else:
            length = len(s)
        return length
