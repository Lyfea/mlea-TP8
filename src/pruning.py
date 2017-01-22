import tree

def pruning(tree):
    if len(tree.sons) == 0:
        return tree.error

    error_sons = 0
    for son in tree.sons:
        error_sons += pruning(son)

    if tree.error <= error_sons:
        tree.sons = []
        tree.chosen_one = -1
        return tree.error

    return error_sons
