"""
TaskManager class - Manages all tasks
"""

import json
from task import Task

class TaskManager:
    def __init__(self):
        self.tasks = []
        
    def add_task(self, task):
        self.tasks.append(task)
        
    def view_all_tasks(self):
        if not self.tasks:
            print("\nNo tasks found!")
            return
            
        print("\n" + "-"*80)
        print("YOUR TASKS:")
        print("-"*80)
        for task in self.tasks:
            print(task)
        print("-"*80)
        
    def mark_completed(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                task.mark_completed()
                return True
        print("Task not found!")
        return False
        
    def delete_task(self, task_id):
        for i, task in enumerate(self.tasks):
            if task.id == task_id:
                self.tasks.pop(i)
                return True
        print("Task not found!")
        return False
        
    def save_tasks(self):
        tasks_data = [task.to_dict() for task in self.tasks]
        with open("tasks.json", "w") as f:
            json.dump(tasks_data, f, indent=4)
            print("✓ Tasks saved to file!")
            
    def load_tasks(self):
        try:
            with open("tasks.json", "r") as f:
                tasks_data = json.load(f)
            self.tasks = []
            for task_data in tasks_data:
                task = Task(task_data["title"], task_data["description"], task_data["priority"])
                task.id = task_data["id"]
                task.completed = task_data["completed"]
                self.tasks.append(task)
                if task.id >= Task.task_counter:
                    Task.task_counter = task.id + 1
        except FileNotFoundError:
            print("✗ No saved tasks found!")
        except Exception as e:
            print(f"✗ Error loading tasks: {e}")
