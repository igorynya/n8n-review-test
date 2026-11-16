"""Простой учебный модуль: калькулятор и работа со списком задач."""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Деление на ноль")
    return a / b


def average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


class TodoList:
    def __init__(self):
        self.items = []

    def add(self, title):
        self.items.append({"title": title, "done": False})

    def complete(self, index):
        self.items[index]["done"] = True

    def pending(self):
        return [item for item in self.items if not item["done"]]


def main():
    print("2 + 3 =", add(2, 3))
    print("10 / 4 =", divide(10, 4))
    print("average:", average([1, 2, 3, 4]))

    todo = TodoList()
    todo.add("Написать код")
    todo.add("Открыть PR")
    todo.complete(0)
    print("Осталось:", todo.pending())


if __name__ == "__main__":
    main()
