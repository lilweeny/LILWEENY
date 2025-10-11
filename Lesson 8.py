class Task:

    """Класс, представляющий задачи"""

    def __init__(self, name):
        self.name = name

class TaskQueue:

    """Класс, представляющий очередь задач"""

    def __init__(self):
        self.tasks = []

    def add_task(self, task):

        """Метод, который добавляет задачу в конец очереди"""

        self.tasks.append(task)

    def get_next_task(self):

        """Метод, который извлекает и возвращает задачу из начала очереди

        :return: None: Если очередь пуста
        """

        if self.is_empty():
            return None
        return self.tasks.pop(0)

    def is_empty(self):

        """Метод, который проверяет, пуста ли очередь"""

        return len(self.tasks) == 0

# Пример использования и тестирования
queue = TaskQueue()

task1 = Task("Задача 1")
task2 = Task("Задача 2")
task3 = Task("Задача 3")

queue.add_task(task1)
queue.add_task(task2)
queue.add_task(task3)

next_task = queue.get_next_task()
print(f"Следующая задача: {next_task.name if next_task else 'Нет задач'}")

queue.get_next_task()

print(f"Очередь пуста: {queue.is_empty()}")