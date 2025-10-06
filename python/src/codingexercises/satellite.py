from typing import Any


def tree_from_traversals(preorder: list[str], inorder: list[str]) -> dict[str, Any]:
    if len(preorder) != len(inorder):
        raise ValueError("traversals must have the same length")
    if set(preorder) != set(inorder):
        raise ValueError("traversals must have the same elements")
    if len(set(preorder)) != len(preorder):
        raise ValueError("traversals must contain unique items")

    if not preorder:
        return {}
    # if len(preorder) == 1:
    #     return {"v": preorder[0], "l": {}, "r": {}}

    val = preorder[0]
    pos = inorder.index(val)

    return {
        "v": val,
        "l": tree_from_traversals(preorder[1 : pos + 1], inorder[0:pos]),
        "r": tree_from_traversals(preorder[pos + 1 :], inorder[pos + 1 :]),
    }
