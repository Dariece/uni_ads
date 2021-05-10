class NodeLeftRight:
    def __init__(self, key, left=None, right=None, father=None):
        self.key = key
        self.left = left
        self.right = right
        self.father = father

    def set_left(self, left):
        self.left = left

    def set_right(self, right):
        self.right = right

    def set_father(self, father):
        self.father = father


class NodeChildBrother:
    def __init__(self, key, left_child=None, right_brother=None, father=None):
        self.key = key
        self.left_child = left_child
        self.right_brother = right_brother
        self.father = father

    def set_left_child(self, left_child):
        self.left_child = left_child

    def set_right_brother(self, right_brother):
        self.right_brother = right_brother

    def set_father(self, father):
        self.father = father


def build_tree() -> NodeLeftRight:
    ret_val = NodeLeftRight(18, father=None)

    ret_val.set_left(NodeLeftRight(12,
                                   NodeLeftRight(7),
                                   NodeLeftRight(4), father=ret_val))

    ret_val.set_right(NodeLeftRight(10, father=ret_val))

    return ret_val


def print_tree(tree: NodeLeftRight, count=0):
    if tree is not None:
        print(''.join(' ' for i in range(count)), tree.key)
        count += 1
        print_tree(tree.left, count)
        print_tree(tree.right, count)


print_tree(build_tree())
