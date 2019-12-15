from listnode import ListNode
from solution import Solution

if __name__ == '__main__':
    # l1: ListNode 2 -> 4 -> 3
    l1 = ListNode(2)
    l1_2 = ListNode(3)
    l1_1 = ListNode(4)
    l1_1.next = l1_2
    l1.next = l1_1

    # l2: ListNode 5 -> 6 -> 4
    l2 = ListNode(5)
    l2_2 = ListNode(4)
    l2_1 = ListNode(6)
    l2_1.next = l2_2
    l2.next = l2_1

    sol = Solution()
    print(sol.addTwoNumbers(l1, l2))

