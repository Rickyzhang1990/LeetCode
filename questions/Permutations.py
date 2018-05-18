class Solution:
    def permute(self, nums , n_li = [],result = []):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 1: 
            n_li.append(nums[0])
            result.append(n_li)
        else:
            for x in nums:
                num_tem = nums[:]
                n_li.append(x)
                num_tem.remove(x)
                self.permute(num_tem,n_li,result)
        return result
