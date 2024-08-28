class ListNode:
    def __init__(self , val):
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

    def append(self,val):
        pass
        

sol = Solution()


