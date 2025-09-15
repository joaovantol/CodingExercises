from typing import Any


class Zipper:
    def __init__(self, tree: Any, parent: Any) -> None:
        self.tree = tree
        self.parent = parent
        self.current = self

    @staticmethod
    def from_tree(tree: Any) -> "Zipper":
        return Zipper(tree, parent=None)

    def value(self) -> Any:
        if self.tree:
            return self.tree.get("value")

    def set_value(self, value: Any) -> Any:
        self.tree.update({"value": value})

        return self

    def left(self) -> "Zipper | None":
        if self.tree.get("left"):
            return Zipper(self.tree.get("left"), self)
        else:
            return None

    def right(self) -> "Zipper | None":
        if self.tree.get("right"):
            return Zipper(self.tree.get("right"), self)
        else:
            return None

    def set_left(self, left: Any) -> Any:
        self.tree.update({"left": left})

        return self

    def set_right(self, right: Any) -> Any:
        self.tree.update({"right": right})
        return self

    def up(self) -> Any | None:
        if self.parent is not None:
            self.tree = self.parent.tree
            self.parent = self.parent.parent

            return self
        else:
            return None

    def to_tree(self) -> Any:
        while self.current.parent:
            self.current = self.current.parent

        return self.current.tree
