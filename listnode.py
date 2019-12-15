class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return "ListNode{val: " + str(self.val) +  ", next: " + str(self.next) + "}"
