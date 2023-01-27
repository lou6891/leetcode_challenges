'''
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

 

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
'''

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        class ListNode:
                def __init__(self, val=0, next=None):
                    self.val = val
                    self.next = next

        temp = []
        
        for linklist in lists:
            while linklist != None:
                temp.append(linklist.val)
                linklist = linklist.next

        temp.sort(reverse=True)
        
        

        if len(temp) > 0:
            #print(temp)            
            
            head = None
            for x in temp:
                head = ListNode(x, next=head)

            return head
        
        else:
            return ListNode("")