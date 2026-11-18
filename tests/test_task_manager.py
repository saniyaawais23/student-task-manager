import unittest
from task_manager import TaskManager


class TestTaskManager(unittest.TestCase):
    def setUp(self):
        self.manager = TaskManager()

    def test_add_task(self):
        self.manager.add_task("Study DevOps")
        tasks = self.manager.list_tasks()
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0]["title"], "Study DevOps")

    def test_complete_task(self):
        task = self.manager.add_task("Write report")
        self.assertTrue(self.manager.complete_task(task["id"]))
        self.assertTrue(self.manager.list_tasks()[0]["completed"])

    def test_delete_task(self):
        task = self.manager.add_task("Temporary task")
        self.manager.delete_task(task["id"])
        self.assertEqual(self.manager.list_tasks(), [])

    def test_empty_title_rejected(self):
        with self.assertRaises(ValueError):
            self.manager.add_task("   ")

    def test_delete_invalid_id(self):
        with self.assertRaises(ValueError):
            self.manager.delete_task(99)


if __name__ == "__main__":
    unittest.main()