from typing import Any


class TreeNode:
    """
    A node in a binary search tree.

    Attributes:
        data: The value stored in the node
        left: Reference to the left child node
        right: Reference to the right child node
    """

    def __init__(
        self, data: Any, left: Any | None = None, right: Any | None = None
    ) -> None:
        """
        Initialize a new tree node.

        Args:
            data: The value to store in this node
            left: Left child node (default: None)
            right: Right child node (default: None)
        """
        self.data = data
        self.left = left
        self.right = right

    def __str__(self) -> str:
        """String representation of the node for debugging."""
        return f"TreeNode(data={self.data}, left={self.left}, right={self.right})"


class BinarySearchTree:
    """
    A binary search tree implementation.

    A binary search tree is a rooted binary tree where:
    - The left subtree of a node contains only nodes with data less than the node's data
    - The right subtree of a node contains only nodes with data greater than the node's data
    - Both left and right subtrees must also be binary search trees

    Attributes:
        root: The root node of the tree
    """

    def __init__(self, tree_data: list[Any]) -> None:
        """
        Initialize a binary search tree from a list of data.

        Args:
            tree_data: List of values to insert into the tree
        """
        self.root = TreeNode(tree_data[0])
        for data in tree_data[1:]:
            self.insert(data)

    def insert(self, data: float) -> None:
        """
        Insert a new value into the binary search tree.

        Args:
            data: The value to insert

        Time Complexity: O(h) where h is the height of the tree
        (O(log n) for balanced trees, O(n) for unbalanced trees)
        """
        self.root = self._insert_recursive(self.root, data)

    def _insert_recursive(self, node: TreeNode | None, data: float) -> TreeNode:
        """
        Recursive helper method for inserting a value into the tree.

        Args:
            node: Current node being examined
            data: Value to insert

        Returns:
            The node (possibly updated with new children)
        """
        if node is None:
            return TreeNode(data)

        if data <= node.data:
            node.left = self._insert_recursive(node.left, data)
        else:
            node.right = self._insert_recursive(node.right, data)

        return node

    def data(self) -> TreeNode:
        """
        Get the root node of the tree.

        Returns:
            The root TreeNode or None if tree is empty
        """
        return self.root

    def sorted_data(self) -> list[Any]:
        """
        Get all data from the tree in sorted order (ascending).

        Returns:
            List of data values in sorted order

        Time Complexity: O(n) where n is the number of nodes
        """
        result: list[Any] = []
        self.tree_ordering(self.root, result)
        return result

    def tree_ordering(self, node: TreeNode | None, result: list[Any]) -> None:
        """
        Perform an in-order traversal to collect data in sorted order.

        In-order traversal: left subtree -> current node -> right subtree

        Args:
            node: Current node being visited
            result: List to accumulate the sorted data
        """
        if node is not None:
            self.tree_ordering(node.left, result)
            result.append(node.data)
            self.tree_ordering(node.right, result)
