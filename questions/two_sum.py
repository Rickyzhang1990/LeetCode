class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for i in range(0,len(nums)):
            le = target - nums[i]
            if le in dic:
                return [dic[le] , i]
            else:
                dic[nums[i]] = i
