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