class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        lineA = "QWERTYUIOP"
        lineB = "ASDFGHJKL"
        lineC = "ZXCVBNM"
        result = []
        for word in words:
            letters = list(word)
            resultA = []
            resultB = []
            resultC = []
            for letter in letters:
                if letter.upper() in lineA:
                    resultA.append(1)
                else:   resultA.append(0)
                if letter.upper() in lineB: 
                    resultB.append(1)
                else:   resultB.append(0)
                if letter.upper() in lineC: 
                    resultC.append(1)
                else:   resultC.append(0)
            if any([all(resultA),all(resultB),all(resultC)]):
                result.append(word)
        return result 
