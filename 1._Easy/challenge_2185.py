class Solution(object):
    def prefixCount(self, words, pref):
        """
        :type words: List[str]
        :type pref: str
        :rtype: int
        """
        
        x = slice(0,len(pref))
        counter = 0
        for word in words:
            if word[x] == pref:
                counter = counter + 1
        
        return counter