from typing import Tuple
from listnode import ListNode

class Solution:

    def add(self, e1: int, e2: int, c: int) -> Tuple[int, int]:
        result = (e1 + e2 + c) % 10
        carry = int((e1 + e2 + c) / 10)
        return result, carry
    
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # variable to store the carry from the lower place
        carry = 0
        # prepare the head node of the result
        result, carry = self.add(l1.val, l2.val, 0)
        head = ListNode(result)
        # variable to store the current node of the result
        cur = head
        # variable to store the object of l1 and l2 temporary
        p, q = l1.next, l2.next
        # while p and q don't reach the end of the list
        while p != None and q != None:
            # print("in the first while")
            result, carry = self.add(p.val, q.val, carry)
            next = ListNode(result)
            cur.next = next
            cur = cur.next
            p = p.next
            q = q.next

        # while one of p or q is still not reach the end
        while p != None or q != None:
            # if no more q but p is remaining
            if p != None:
                # add p.val and the carry from the lower place
                res, carry = self.add(p.val, 0, carry)
                # append the upper place result and update the cur pointer
                cur.next = ListNode(res)
                cur = cur.next
                # update the p pointer
                p = p.next
            # if no more p but q is remaining    
            elif q != None:
                # add q.val and the carry from the lower place
                res, carry = self.add(q.val, 0, carry)
                # append the upper place result and update the cur pointer
                cur.next = ListNode(res)
                cur = cur.next
                # update the q pointer
                q = q.next

        # if remaining carry, append it to the upper place
        if carry != 0:
            cur.next = ListNode(carry)

        # return the head of the list
        return head
        
