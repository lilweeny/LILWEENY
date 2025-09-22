class Stack:
    """
    Класс, отвечающий за формирования стека данных
    """
    def __init__(self):
        """
        Метод, инициализирующий стек
        """
        self.items = []

    def push(self, value):
        """
        Метод, добавляющий элемент в стек
        :param value:
        :return:
        """
        self.items.append(value)

    def pop(self):
        """
        Метод, удаляющий и возвращающий элемент из вершины стека

        :return: Элемент вершины стека

        :raises IndexError: Если стек пуст
        """
        if not self.items:
            raise IndexError("Стек пуст")
        return self.items.pop()

    def peek(self):
        """
        Метод, возвращающий элемент вершины стека

        :return: Элемент вершины стека
        :return: None: Если стек пуст
        """
        if not self.items:
            return None
        return self.items[-1]

    def is_empty(self):
        """
        Метод, возвращающий длину стека

        :return: Длина стека
        """
        return len(self.items) == 0

def couple(s: str) -> bool:
    """
    Функция, которая проверяет корректность скобочной последовательности в строке

    :param s: Строка скобок
    :return: True: Если все скобки в строке вложены правильно
    :return: False: Если имеется некорректность ввода или последовательности скобок в строке
    """
    braces = {'(': ')', '{': '}', '[': ']'}
    closing = set(braces.values())
    stack = Stack()

    for br in s:
        if br in braces:
            stack.push(br)
        elif br in closing:
            top = stack.peek()
            if top is None:
                return False
            if braces[top] != br:
                return False
            stack.pop()
        else:
            continue
    return stack.is_empty()
