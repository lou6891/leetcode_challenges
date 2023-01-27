'''
A pangram is a sentence where every letter of the English alphabet appears at least once.

Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.

 

Example 1:

Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
Output: true
Explanation: sentence contains at least one of every letter of the English alphabet.
'''

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
        