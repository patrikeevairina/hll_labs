class TreeNode:
    def __init__(self, val):
        self.value = val
        # self.parent = None
        self.left = None
        self.right = None

    def has_req_child(self, val):
        if self.value > val and self.left is not None:
            return True
        elif self.value < val and self.right is not None:
            return True
        return False

    def append_child(self, value):
        if self.value > value:
            self.left = TreeNode(value)
            # self.left.parent = self
        elif self.value < value:
            self.right = TreeNode(value)
            # self.right.parent = self

    def __str__(self):
        return "{0}".format(self.value)

    def __iter__(self):
        if self.left is not None:
            yield from self.left
        yield self
        if self.right is not None:
            yield from self.right


class Tree:
    def __init__(self):
        self.root = None

    def add_value(self, value):
        if self.root is None:
            self.root = TreeNode(value)
            return

        current_node = self.root
        while current_node.has_req_child(value):
            current_node = current_node.left if current_node.value > value else current_node.right

        current_node.append_child(value)

    def print(self):
        self.print_node(self.root)

    def print_node(self, node):
        if node is None:
            return
        self.print_node(node.left)
        print(node.value)
        self.print_node(node.right)

    def __iter__(self):
        yield from self.root


t = Tree()
l = (10, 1, 2, 4, 6, 15, 1, 1, 1, 3, 20, 45, 19)

for i in l:
    t.add_value(i)
for i in t:
    print(i)
