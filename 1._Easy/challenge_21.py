''''
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

 

Example 1:

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
'''

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        class ListNode:
            def __init__(self, val=0, next=None):
                self.val = val
                self.next = next

        temp = []

        while list1:
            temp.append(list1.val)
            list1 = list1.next

        while list2:
            temp.append(list2.val)
            list2 = list2.next

        temp.sort(reverse=True)

        #print(temp)

        out = None

        for i in temp:
            out = ListNode(i, next=out)

        return out