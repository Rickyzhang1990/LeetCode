#python2 
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        dic = {}
        result = ""
        for letter in s:
            if letter in dic:
                dic[letter] += 1 
            else:
                dic[letter] = 1 
        for i,j in sorted(dic.iteritems(),lambda x, y: cmp(x[1], y[1]), reverse=True):
            result += i*j
        return result 
 
 #python3
 class Solution:
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        dic = {}
        result = ""
        for letter in s:
            if letter in dic:
                dic[letter] += 1 
            else:
                dic[letter] = 1 
        for i,j in sorted(zip(dic.keys(),dic.values()) ,key = lambda x:x[1],reverse = True):
            result += i*j
        return result 
   '''python3中取消了dic.iteritems()函数，如果要进行排序，需要先使用zip函数将字典的键值对转化成一一对应的列表，然后使用匿名函数lambda对zip后的列表  
   进行排序，得到排序后的列表后再进行遍历，得到排序后的字符组成，总体来说这道题应该不是medium的难度，比较简单'''
