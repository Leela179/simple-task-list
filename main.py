#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f'Task "{task}" added successfully.')

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print(f'Task "{task}" removed successfully.')
        else:
            print(f'Task "{task}" not found.')

    def list_tasks(self):
        if not self.tasks:
            print('No tasks found.')
        else:
            print('Task List:')
            for idx, task in enumerate(self.tasks, start=1):
                print(f'{idx}. {task}')

    def prioritize_task(self, task, priority):
        if task in self.tasks:
            self.tasks.remove(task)
            self.tasks.insert(priority - 1, task)
            print(f'Task "{task}" prioritized to position {priority}.')
        else:
            print(f'Task "{task}" not found.')

    def recommend_task(self, keyword):
        matching_tasks = [task for task in self.tasks if keyword.lower() in task.lower()]
        if matching_tasks:
            print(f'Task recommendations for "{keyword}":')
            for idx, task in enumerate(matching_tasks, start=1):
                print(f'{idx}. {task}')
        else:
            print(f'No tasks found with the keyword "{keyword}".')

# Example usage:
if __name__ == "__main__":
    task_manager = TaskManager()

    while True:
        print("\nTask Management App Menu:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. List Tasks")
        print("4. Prioritize Task")
        print("5. Task Recommendations")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            task = input("Enter task description: ")
            task_manager.add_task(task)
        elif choice == "2":
            task = input("Enter task description to remove: ")
            task_manager.remove_task(task)
        elif choice == "3":
            task_manager.list_tasks()
        elif choice == "4":
            task = input("Enter task description to prioritize: ")
            priority = int(input("Enter new priority position: "))
            task_manager.prioritize_task(task, priority)
        elif choice == "5":
            keyword = input("Enter a keyword for task recommendations: ")
            task_manager.recommend_task(keyword)
        elif choice == "6":
            print("Exiting Task Management App. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")


# In[1]:


1


# In[ ]:




