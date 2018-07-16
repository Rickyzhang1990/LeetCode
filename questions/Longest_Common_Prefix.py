class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) > 1  and strs[0] != "":
            target = ""
            min_len = min([len(x) for x in strs])
            for i in range(min_len):
                prefix = [x[i] for x in strs]
                if len(set(prefix)) == 1:
                    target += strs[0][i]
                else:
                    return target
            return target
        elif len(strs) == 1 and strs[0] != "":
            return strs[0]
        else:   return ""
