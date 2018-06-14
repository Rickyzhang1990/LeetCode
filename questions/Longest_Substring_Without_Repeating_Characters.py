class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0: return 0   #当时报错字符串为空时，会报下标越界错误
        else:
            substr=""
            result = []
            for x in s:
                if not x in substr:
                    substr += x 
                else:
                    if x != substr[-1]:
                        result.append(substr)
                        substr = substr.replace(substr[:substr.index(x) + 1 ],"")  #解决当字符串为“dvdf”以及“ckilbkd”出现的错误
                        substr += x 
                    else:
                        result.append(substr)
                        substr = x 
            result.append(substr)                #解决字符串长度为1时，会报max没有参数传入的问题
            return max([len(i) for i in result])
