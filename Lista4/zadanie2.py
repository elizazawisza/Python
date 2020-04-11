import random

i = 0


def getRootVal(root):
    return root[0]


def getLeftChild(root):
    return root[1]


def getRightChild(root):
    return root[2]


def createList(first, last):
    return [item for item in range(first, last)]


def generateBinaryTree(tree_size, tree_nodes):
    if size == 0:
        return None

    global i
    if i < len(tree_nodes):
        node_value = tree_nodes[i]
        i += 1
    else:
        return None
    left_subtree = generateBinaryTree(tree_size - 1, tree_nodes)
    right_subtree = generateBinaryTree(tree_size - 1, tree_nodes)

    side_choice = random.choice(['insertLeft', 'insertRight'])

    if side_choice == 'insertLeft':
        return [node_value, left_subtree, right_subtree]
    else:
        return [node_value, right_subtree, left_subtree]


def dfs(tree):
    if tree is None:
        return
    yield getRootVal(tree)
    yield from dfs(getLeftChild(tree))
    yield from dfs(getRightChild(tree))


def bfs(tree):
    if tree is None:
        return
    subtrees = [tree]
    while len(subtrees) > 0:
        tmp_subtrees = []
        for subtree in subtrees:
            if subtree is None:
                continue
            yield getRootVal(subtree)
            tmp_subtrees.append(getLeftChild(subtree))
            tmp_subtrees.append(getRightChild(subtree))
        subtrees = tmp_subtrees


if __name__ == '__main__':
    size = 4
    number_of_elements = random.randint(2 ** (size - 1) + 1, 2 ** size)
    elements = createList(1, number_of_elements)
    binary_tree = generateBinaryTree(size, elements)
    print(binary_tree)
    print(list(dfs(binary_tree)))
    print(list(bfs(binary_tree)))
