from typing import Any

class SgfTree:
    """
    Represents a node in an SGF (Smart Game Format) game tree.

    Attributes:
        properties (dict): A dictionary mapping property keys to their values.
        children (list): A list of child SgfTree nodes.
    """
    def __init__(self, properties: (dict | Any) = None, children: (Any | None) = None) -> None:
        """
        Initializes an SgfTree node.

        Args:
            properties (dict): Dictionary of properties for this node.
            children (list): List of child nodes.
        """
        self.properties = properties or {}
        self.children = children or []

    def __eq__(self, other: Any) -> bool:
        """
        Compares two SgfTree nodes for equality.

        Args:
            other (SgfTree): The other node to compare with.

        Returns:
            bool: True if nodes are equal, False otherwise.
        """
        if not isinstance(other, SgfTree):
            return False
        for key, value in self.properties.items():
            if key not in other.properties:
                return False
            if other.properties[key] != value:
                return False
        for key in other.properties.keys():
            if key not in self.properties:
                return False
        if len(self.children) != len(other.children):
            return False
        for child, other_child in zip(self.children, other.children):
            if child != other_child:
                return False
        return True

    def __repr__(self) -> str:
        """
        Returns a string representation of the SGF tree.
        """
        return f"SgfTree(properties={self.properties}, children={self.children})"


def parse(input_string: str) -> "SgfTree":
    """
    Parses an SGF string and returns the corresponding SGF tree.

    Args:
        input_string (str): The SGF string to parse.

    Returns:
        SgfTree: The root node of the parsed SGF tree.

    Raises:
        ValueError: If the input string is not a valid SGF format.
    """
    if not input_string:
        raise ValueError("tree missing")

    # The input must start with '(' and end with ')'
    if not (input_string.startswith('(') and input_string.endswith(')')):
        raise ValueError("tree missing")

    # Remove the outer parentheses
    input_string = input_string[1:-1].strip()

    if not input_string:
        raise ValueError("tree with no nodes")

    # The first character must be ';'
    if not input_string.startswith(';'):
        raise ValueError("tree missing")

    # Parse the nodes
    nodes = []
    pos = 0
    while pos < len(input_string):
        if input_string[pos] == ';':
            pos += 1
            properties = {}

            # Parse properties until we hit a ';' or '(' or end of string
            while pos < len(input_string) and input_string[pos] not in ';(':
                # Property starts with a key
                key_start = pos
                while pos < len(input_string) and input_string[pos].isupper():
                    pos += 1

                if pos == key_start:
                    raise ValueError("property must be in uppercase")

                key = input_string[key_start:pos]

                # Property must have at least one value
                if pos >= len(input_string) or input_string[pos] != '[':
                    if pos < len(input_string):
                        if input_string[pos].islower():
                            raise ValueError("property must be in uppercase")
                    else:
                        raise ValueError("properties without delimiter")

                values = []
                while pos < len(input_string) and input_string[pos] == '[':
                    pos += 1
                    value_start = pos
                    escaped = False

                    # Find the closing ']', handling escaped characters
                    while pos < len(input_string):
                        if not escaped and input_string[pos] == '\\':
                            escaped = True
                            pos += 1
                            continue
                        if not escaped and input_string[pos] == ']':
                            break
                        escaped = False
                        pos += 1

                    if pos >= len(input_string):
                        raise ValueError("unclosed property value")

                    value = input_string[value_start:pos]
                    # Unescape the value (replace escaped characters)
                    value = value.replace('\\]', ']').replace('\\\t', " ").replace('\\\n', "").replace('\\\\', '\\')
                    value = value.replace('\t', " ")
                    value = value.replace('\\n', 'n').replace('\\t', 't')
                    values.append(value)
                    pos += 1  # skip the closing ']'

                if not values:
                    raise ValueError("property must have at least one value")

                properties[key] = values

            nodes.append(SgfTree(properties))
        elif input_string[pos] == '(':
            # Start of a child subtree
            subtree_end = find_matching_parenthesis(input_string, pos)
            try:
                subtree = parse(input_string[pos:subtree_end+1])
            except ValueError as e:
                raise ValueError(str(e))
            if nodes:
                nodes[-1].children.append(subtree)
            else:
                raise ValueError("tree missing")
            pos = subtree_end + 1
        else:
            # Skip whitespace between nodes
            if input_string[pos].isspace():
                pos += 1
            else:
                raise ValueError("tree missing")

    if not nodes:
        raise ValueError("tree missing")

    # The first node is the root, and any subsequent nodes are its children
    root = nodes[0]
    for node in nodes[1:]:
        root.children.append(node)

    return root


def find_matching_parenthesis(s: str, start: int) -> int:
    """
    Fins the position of the closing parenthesis matching the one at 'start'.

    Args:
        s (str): The string to search in.
        start (int): The position of the opening parenthesis.

    Returns:
        int: The position of the matching closing parenthesis.

    Raises:
        ValueError: If no matching parenthesis is found.
    """
    if start >= len(s) or s[start] != '(':
        raise ValueError("tree missing")

    depth = 1
    pos = start + 1

    while pos < len(s) and depth > 0:
        if s[pos] == '(':
            depth += 1
        elif s[pos] == ')':
            depth -= 1
        pos += 1

    if depth != 0:
        raise ValueError("unclosed tree")

    return pos - 1
