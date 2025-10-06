from typing import Any


def tree_from_traversals(
    preorder: list[str],
    inorder: list[str],
    check_warnings: bool = True,
) -> dict[str, Any]:
    """
    Builds a tree from its pre-order and in-order traversals.

    Args:
        preorder (list): The pre-order traversal
        inorder (list): The in-order traversal
        check_warnings (bool): whether to check the consistency or not

    Returns:
        dict: A dictionary containing the tree
    """
    if check_warnings:
        check(preorder, inorder)

    if not preorder:
        return {}

    val = preorder[0]
    pos = inorder.index(val)

    return {
        "v": val,
        "l": tree_from_traversals(
            preorder[1 : pos + 1],
            inorder[0:pos],
            check_warnings=False,
        ),
        "r": tree_from_traversals(
            preorder[pos + 1 :],
            inorder[pos + 1 :],
            check_warnings=False,
        ),
    }


def check(
    preorder: list[str],
    inorder: list[str],
) -> None:
    """
    Raises an error if the in-order traversal and pre-order traversal are not
    consistent to build a tree.

    Args:
        preorder (list): The pre-order traversal
        inorder (list): The in-order traversal
    """
    if len(preorder) != len(inorder):
        raise ValueError("traversals must have the same length")
    if set(preorder) != set(inorder):
        raise ValueError("traversals must have the same elements")
    if len(set(preorder)) != len(preorder):
        raise ValueError("traversals must contain unique items")
