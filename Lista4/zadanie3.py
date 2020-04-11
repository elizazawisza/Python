import random


class Node(object):
    def __init__(self, value, children):
        self.value = value
        self.children = children

    def getNodeValue(self):
        return self.value

    def __str__(self):
        return str(self.value) + ',  [' + ' , '.join(map(str, self.children)) + ']'


def generateBinaryTree(tree_size:int):
    if tree_size == 0:
        return None
    elif tree_size == 1:
        return Node(1, [])

    node_value = random.randint(2 ** (tree_size - 1) + 1, 2 ** tree_size)
    amount_of_children = random.randint(1, 2)
    subtrees = []

    for i in range(0, amount_of_children):
        side_choice = random.choice(['insertLeft', 'insertRight'])
        if side_choice == 'insertLeft':
            tree = generateBinaryTree(random.randint(1, tree_size - 1))
        else:
            tree = generateBinaryTree(tree_size - 1)
        subtrees.append(tree)
    return Node(node_value, subtrees)


def dfs(tree):
    yield tree.getNodeValue()
    for children in tree.children:
        yield from dfs(children)


def bfs(tree):
    subtrees = [tree]
    while len(subtrees) > 0:
        tmp_subtrees = []
        for subtree in subtrees:
            yield subtree.getNodeValue()
            for node in subtree.children:
                tmp_subtrees.append(node)
        subtrees = tmp_subtrees.copy()


def createList(first, last):
    return [item for item in range(first, last)]


if __name__ == '__main__':
    size = 5
    binary_tree = generateBinaryTree(size)
    print(str(binary_tree))
    print(list(dfs(binary_tree)))
    print(list(bfs(binary_tree)))
