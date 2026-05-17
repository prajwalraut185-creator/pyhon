"""
Task class - Represents a single task
"""

class Task:
    task_counter = 1
    
    def __init__(self, title, description, priority):
        self.id = Task.task_counter
        Task.task_counter += 1
        self.title = title
        self.description = description
        self.priority = priority
        self.completed = False
        
    def mark_completed(self):
        self.completed = True
        
    def __str__(self):
        status = "✓ Completed" if self.completed else "○ Pending"
        return f"[{self.id}] {self.title} | {self.description} | Priority: {self.priority} | {status}"
    
    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "priority": self.priority,
            "completed": self.completed
        }
