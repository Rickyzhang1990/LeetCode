class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        jewel = list(J)
        count = 0 
        for x in list(S):
            if x in jewel:
                count +=1 
        return count 
