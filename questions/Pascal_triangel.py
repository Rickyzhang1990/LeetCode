class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        L=[]
        for x in range(numRows):
            if x is 0:
                L.append([1])
            else:
                tem_list = L[x-1][:]    
                tem_list.append(0)      
                new = []
                for i in range(x+1):    
                    st = tem_list[i] + tem_list[i-1]  
                    new.append(st)
                L.append(new)
        return L 
