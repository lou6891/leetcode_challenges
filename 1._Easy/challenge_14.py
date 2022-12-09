class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        counter = 1

        if len(strs) == 1:
            return strs[0]
        
        for i in strs:
            if i == "":
                return ""

        max_l = max(strs, key=len)

        while True and counter < len(max_l)+1:
            
            actor = strs[0][:counter]
            tester = 0

            for i in strs:
                if i[:counter] == actor:
                    tester +=1
            
            if tester == len(strs):
                counter += 1
            else:
                break

        if counter > 0:
            return strs[0][:counter -1]
        else:
            return ""