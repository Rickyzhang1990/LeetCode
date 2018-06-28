class Solution:
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        a = list(str(num))
        large = num 
        for x in range(len(a)):
            for y in range(len(a) -x):
                a[x],a[x+y] = a[x+y],a[x]
                new_n = int("".join(a))
                large = new_n if new_n > large else large  
                a = list(str(num))
        return large         
