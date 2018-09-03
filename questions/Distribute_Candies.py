class Solution:
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        receive_nu = len(candies)/2
        kinds = len(set(candies))
        nu = receive_nu if receive_nu < kinds else kinds
        return int(nu) 
#题目思路简单，如果糖果种类大于糖果数目的1/2，那么只能得到糖果数目一半的种类，如果糖果种类小于糖果数目的1/2，那么可以获得所有种类的糖果。
