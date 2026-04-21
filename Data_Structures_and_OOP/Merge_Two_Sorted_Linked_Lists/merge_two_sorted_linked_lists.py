# Definition for the List Node class.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        # Create a dummy node to act as the starting point
        dummy = ListNode()
        current = dummy

        # Iterate while both lists have nodes
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            
            # Move the current pointer forward
            current = current.next

        # If one list is finished, attach the remaining part of the other list
        current.next = list1 if list1 else list2

        # The actual head is the node after the dummy
        return dummy.next