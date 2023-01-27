"""
Given a valid (IPv4) IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]".

 

Example 1:

Input: address = "1.1.1.1"
Output: "1[.]1[.]1[.]1"
"""

class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        address = list(address)
        ret_address = []

        for i,v in enumerate(address):
            if v == ".":
                ret_address.append("[")
                ret_address.append(".")
                ret_address.append("]")
            else:
                ret_address.append(v)

        ret_address = ''.join(str(x) for x in ret_address)

        return(ret_address)