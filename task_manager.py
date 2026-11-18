class TaskManager:
    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def add_task(self, title):
        if title is None or not title.strip():
            raise ValueError("Task title cannot be empty.")
        task = {"id": self.next_id, "title": title.strip(), "completed": False}
        self.tasks.append(task)
        self.next_id += 1
        return task

    def list_tasks(self):
        return list(self.tasks)

    def complete_task(self, task_id):
        for t in self.tasks:
            if t["id"] == task_id:
                t["completed"] = True
                return True
        return False

    def delete_task(self, task_id):
        for t in self.tasks:
            if t["id"] == task_id:
                self.tasks.remove(t)
                return True
        raise ValueError("Invalid task ID.")