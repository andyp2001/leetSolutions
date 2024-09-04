class Solution(object):
    def countVowels(self, word):
        """
        :type word: str
        :rtype: int
        """
        

        leng = len(word)

        counter = 0


        for i, x in enumerate(word):
            if x in 'aeiou':
                counter += (leng - i) * (i + 1)

        return counter