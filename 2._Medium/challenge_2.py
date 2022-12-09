# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        class ListNode(object):
            def __init__(self, val=0, next=None):
                self.val = val
                self.next = next
        
        
        def loopNL(LN):
            arr = []
            t =LN
            while t :
                if t == None:
                    break;
                arr.append(t.val)
                t = t.next
            return arr
    
        a = loopNL(l1)
        b = loopNL(l2)
        a.reverse()
        b.reverse()
        na = ''.join(str(x) for x in a) 
        nb = ''.join(str(x) for x in b) 
        
        c = str(int(na) + int(nb))
        c = [int(x) for x in c]
        
        
        head = None
        for x in c:
            head = ListNode(x, next=head)
        
        return head
       
            
            
      