class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        # 头部伪节点
        self._head = Node(0)
        self._count = 0

    def get(self, index: int) -> int:
        if 0 <= index < self._count:
            cur = self._head.next
            for _ in range(index):
                cur = cur.next
            return cur.val
        else:
            return -1

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self._count, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0:
            index = 0
        # _count为链表末尾
        elif index > self._count:
            return
        cur = self._head
        for _ in range(index):
            cur = cur.next
        nxt = cur.next
        cur.next = Node(val)
        cur.next.next = nxt
        self._count += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0:
            index = 0
        elif index >= self._count:
            return
        cur = self._head
        for _ in range(index):
            cur = cur.next
        cur.next = cur.next.next
        self._count -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)