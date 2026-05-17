"""
Task Manager - A simple project management system
"""

from task import Task
from task_manager import TaskManager

def display_menu():
    print("\n" + "="*40)
    print("     TASK MANAGER APPLICATION")
    print("="*40)
    print("1. Add a new task")
    print("2. View all tasks")
    print("3. Mark task as completed")
    print("4. Delete a task")
    print("5. Save tasks")
    print("6. Load tasks")
    print("7. Exit")
    print("="*40)

def main():
    manager = TaskManager()
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-7): ").strip()
        
        if choice == "1":
            title = input("Enter task title: ").strip()
            description = input("Enter task description: ").strip()
            priority = input("Enter priority (High/Medium/Low): ").strip()
            task = Task(title, description, priority)
            manager.add_task(task)
            print("✓ Task added successfully!")
            
        elif choice == "2":
            manager.view_all_tasks()
            
        elif choice == "3":
            manager.view_all_tasks()
            try:
                task_id = int(input("Enter task ID to mark as completed: "))
                manager.mark_completed(task_id)
                print("✓ Task marked as completed!")
            except ValueError:
                print("✗ Invalid input!")
                
        elif choice == "4":
            manager.view_all_tasks()
            try:
                task_id = int(input("Enter task ID to delete: "))
                manager.delete_task(task_id)
                print("✓ Task deleted successfully!")
            except ValueError:
                print("✗ Invalid input!")
                
        elif choice == "5":
            manager.save_tasks()
            print("✓ Tasks saved to file!")
            
        elif choice == "6":
            manager.load_tasks()
            print("✓ Tasks loaded from file!")
            
        elif choice == "7":
            print("Thank you for using Task Manager! Goodbye!")
            break
            
        else:
            print("✗ Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
