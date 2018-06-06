class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        lineA = ["Q","q","W","w","E","e","R","r","T","t","Y","y","U","u","I","i","O","o","P","p"]
        lineB = ["A","a","S","s","D","d","F","f","G","g","H","h","J","j","K","k","L","l"]
        lineC = ["Z","z","X","x","C","c","V","v","B","b","N","n","M","m"]
        result = []
        for word in words:
            letters = list(word)
            resultA = []
            resultB = []
            resultC = []
            for letter in letters:
                if letter in lineA:
                    resultA.append(1)
                else:   resultA.append(0)
                if letter in lineB: 
                    resultB.append(1)
                else:   resultB.append(0)
                if letter in lineC: 
                    resultC.append(1)
                else:   resultC.append(0)
            if any([all(resultA),all(resultB),all(resultC)]):
                result.append(word)
        return result 
