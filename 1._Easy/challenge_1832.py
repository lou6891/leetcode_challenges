class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        dictionary = list(string.ascii_lowercase)
        
        for i in sentence:
            try:
                index =  dictionary.index(i)
                dictionary.pop(index)
            except:
                pass
            
        if len(dictionary) > 0:
            return False
        else:
            return True
        