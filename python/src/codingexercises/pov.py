from typing import Any, Optional


class Tree:
    def __init__(self, name: str, children: Optional[list["Tree"]] = None) -> None:
        self.name = name
        self.children = children if children is not None else []

    def __dict__(self) -> dict[Any, list[Any]]:
        return {self.name: [child.__dict__() for child in sorted(self.children)]}

    def __lt__(self, other: "Tree") -> bool:
        return self.name < other.name

    def __eq__(self, other: "Tree") -> bool:
        return self.__dict__() == other.__dict__()

    def from_pov(self, from_node: str) -> "Tree":
        path = self.child_path(from_node)
        if not path:
            raise ValueError("Tree could not be reoriented")
        for parent, child in zip(path, path[1:]):
            parent.swap(child)

        return path[-1]

    def child_path(self, to_node: str) -> list["Tree"]:
        if self.name == to_node:
            return [self]

        for child in self.children:
            path = child.child_path(to_node)
            if path:
                return [self] + path
        return []

    def swap(self, other: "Tree") -> None:
        self.children.remove(other)
        other.children.append(self)

    def path_to(self, from_node: str, to_node: str) -> list[str]:
        root = self.from_pov(from_node)
        path = root.child_path(to_node)
        if not path:
            raise ValueError("No path found")
        return [node.name for node in path]
