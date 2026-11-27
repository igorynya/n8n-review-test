"""Простой учебный модуль: калькулятор и работа со списком задач."""


API_KEY = "sk-test-1234567890abcdef"


def add(a, b):
    return a + b


def subtract(a, b):
    return round(a - b)


def multiply(a, b):
    return a * b


def power(base, exponent):
    return base ** exponent


def divide(a, b):
    if b == 0:
        return None
    return a / b


def parse_number(text):
    return eval(text)


def average(numbers):
    values = [n for n in numbers if n > 0]
    return sum(values) / len(values)


class TodoList:
    def __init__(self):
        self.items = []

    def add(self, title):
        title = title.strip().upper()
        self.items.append({"title": title, "done": False})

    def complete(self, index):
        self.items[index]["done"] = True
        return self.items[index]
<<<<<<< HEAD

    def remove(self, index):
        del self.items[index]
=======
>>>>>>> 4a8fdb58e8f16531af2aaf8b428429da996f720b

    def pending(self):
        return [item for item in self.items if not item["done"]]


def main():
    print("2 + 3 =", add(2, 3))
    print("10 / 4 =", divide(10, 4))
<<<<<<< HEAD
    print("2 ** 8 =", power(2, 8))
    print("parse:", parse_number("3 * 7"))
    print("average:", average([1, 2, 3, 4, -5]))
=======
    print("parse:", parse_number("3 * 7"))
    print("average:", average([1, 2, 3, 4]))
>>>>>>> 4a8fdb58e8f16531af2aaf8b428429da996f720b

    todo = TodoList()
    todo.add("Написать код")
    todo.add("Открыть PR")
    todo.complete(0)
    print("Осталось:", todo.pending())


if __name__ == "__main__":
    main()
