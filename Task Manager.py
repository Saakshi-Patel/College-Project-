import task , taskw

from datetime import datetime

class Task:
    def __init__(self, title, description, due_date, status='pending'):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

    def __repr__(self):
        return f'Task({self.title}, {self.description}, {self.due_date}, {self.status})'

class TaskManager:
    def __init__(self, filename='tasks.manager'):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        try:
            with open(self.filename, 'r') as f:
                tasks = task.load(f)
        except FileNotFoundError:
            tasks = []
        return tasks

    def save_tasks(self):
        with open(self.filename, 'w') as f:
            taskw.dump(self.tasks, f, indent=4)

    def add_task(self, title, description, due_date):
        task = Task(title, description, due_date)
        self.tasks.append(task)
        self.save_tasks()

    def view_tasks(self, sort_by='due_date'):
        if sort_by == 'due_date':
            self.tasks.sort(key=lambda t: t.due_date)
        elif sort_by == 'priority':
            self.tasks.sort(key=lambda t: t.status)
        for task in self.tasks:
            print(task)

    def update_task(self, index, title=None, description=None, due_date=None, status=None):
        task = self.tasks[index]
        if title:
            task.title = title
        if description:
            task.description = description
