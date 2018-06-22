class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {
            "IV":4,"IX":9,"XL":40,"XC":90,"CM":900,"CD":400,"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000
        }
        result = []
        total = 0 
        while 1: 
            if len(s) >1 :
                if s[:2] in dic: 
                    result.append(s[:2])
                    s = s[2:]
                else:
                    result.append(s[0])
                    s = s[1:]
            else:
                result.append(s)
                break
        for x in result:
            if x != "":
                total += dic[x]
        return total 
