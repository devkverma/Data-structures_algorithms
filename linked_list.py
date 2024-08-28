class ListNode:
    def __init__(self , val = None):
        self.val = val
        self.next = None

class Solution:
    def print(self,linked_list):
        head = linked_list
        print('[',end= '')
        while head.next:
            print(head.val,end=',')
            head = head.next
        else:
            print(head.val,end=']')

    def append(self,linked_list,val):
        head = linked_list
        if head.val is None:
            head.val = val
            return
        while head.next:
            head = head.next
        head.next = ListNode(val)
        return
        

sol = Solution()

l1 = ListNode()
sol.append(l1,5)
sol.print(l1)


