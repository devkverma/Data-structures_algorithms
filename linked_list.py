class ListNode:
    def __init__(self , val = None):
        self.val = val
        self.next = None

class Solution:
    def print(self,linked_list):
        head = linked_list
        stack = []
        print('[',end= '')
        while head.next  and head not in stack:
            print(head.val,end=',')
            stack.append(head)
            head = head.next
        else:
            print(head.val,end=']')
            print()

    def append(self,linked_list,val):
        head = linked_list
        if head.val is None:
            head.val = val
            return
        while head.next:
            head = head.next
        head.next = ListNode(val)
        return
    
    def connectNode(self,linked_list,index):
        head = linked_list
        if head.next is None:
            raise IndexError('List has only one element')
            return
        i = 0
        address = None
        while head.next:
            if i == index:
                address = head
            head = head.next
            i += 1
        if address == None:
            raise IndexError('index out of range')
        else:
            head.next = address
            return
        
    def checkCircular(self,linked_list):
        head = linked_list
        stack = []
        while head.next:
            if head in stack:
                return True
            stack.append(head)
            head = head.next
        return False
        
        

sol = Solution()






