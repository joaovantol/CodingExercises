from json import dumps
from typing import Any, Optional


class Tree:
    def __init__(self, label: str, children: Optional[list["Tree"]] = None) -> None:
        self.label = label
        self.children = children or []

    def __dict__(self) -> dict[Any, list[Any]]:
        return {self.label: [c.__dict__() for c in sorted(self.children)]}

    def __str__(self, indent: None = None) -> str:
        return dumps(self.__dict__(), indent=indent)

    def __lt__(self, other: "True") -> bool:
        return self.label < other.label

    def __eq__(self, other: "Tree") -> bool:
        return self.__dict__() == other.__dict__()

    def from_pov(self, from_node: str) -> "Tree":
        path = self.path_down(from_node)
        if not path:
            raise ValueError("Tree could not be reoriented")
        for parent, child in zip(path, path[1:]):
            parent.swap_with_child(child)

        return path[-1]

    def path_to(self, from_node: str, to_node: str) -> list[str]:
        root = self.from_pov(from_node)
        path = root.path_down(to_node)
        if not path:
            raise ValueError("No path found")
        return [node.label for node in path]

    def path_down(self, to_node: str) -> list["Tree"]:
        if self.label == to_node:
            return [self]

        for c in self.children:
            path = c.path_down(to_node)
            if path:
                return [self] + path
        return []

    def swap_with_child(self, other: "Tree") -> None:
        self.children.remove(other)
        other.children.append(self)
