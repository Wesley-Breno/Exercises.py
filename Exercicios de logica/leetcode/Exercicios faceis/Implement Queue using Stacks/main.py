class MyQueue:
    def __init__(self):
        self.fila = []

    def push(self, x: int) -> None:
        self.fila.append(x)

    def pop(self) -> int:
        e = self.fila[0]
        self.fila.remove(e)
        return e

    def peek(self) -> int:
        return self.fila[0]

    def empty(self) -> bool:
        if self.fila:
            return False
        return True