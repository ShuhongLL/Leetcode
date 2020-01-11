class Node:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end
        self.left = self.right = None
        
class MyCalendar:
    def __init__(self):
        self.root = None

    def book(self, start: int, end: int) -> bool:
        if not self.root:
            self.root = Node(start, end)
            return True
        return self.insert(self.root, Node(start, end))

    def insert(self, root: Node, node: Node):
        if root.end <= node.start:
            if not root.right:
                root.right = node
                return True
            return self.insert(root.right, node)
        elif root.start >= node.end:
            if not root.left:
                root.left = node
                return True
            return self.insert(root.left, node)
        else:
            return False
        

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)