class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):

        """Метод, который добавляет элемент в конец очереди"""

        self.items.append(item)

    def dequeue(self):

        """Метод, который извлекает и возвращает элемент из начала очереди

        :raises IndexError: Если очередь пуста
        """

        if self.is_empty():
            raise IndexError("Попытка извлечения из пустой очереди")
        return self.items.pop(0)

    def is_empty(self):

        """Метод, который проверяет, пуста ли очередь"""

        return len(self.items) == 0

    def size(self):

        """Метод, который возвращает текущий размер очереди"""

        return len(self.items)

queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print("Размер очереди:", queue.size())

while not queue.is_empty():
    item = queue.dequeue()
    print("Извлечен элемент:", item)
