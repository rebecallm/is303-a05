'''
Rebeca Llontop 
IS 303 - A05

Task Manager
This program creates a task list where the user can mark as complete 
or incomplete and separates the tasks by priority level. 

Inputs:
- Task name
- Task category
- Priority level (low, medium, high)

Processes:
- Task: stores a tasks's name, category, and priority level, and completion status
- TaskList: stores tasks in a list, can count incomplete tasks, filter tasks by priority
and can display the full tasks list. 

Outputs: 
- Displayed task list by category along with their incomplete/complete mark and 
priority level. 
'''

class Task:
    def __init__(self, name, category, level):
        self.name = name
        self.category = category
        self.level = level
        self.completion = False  

    def mark_complete(self):
        """Marks the task as completed"""
        self.completion = True 

    def __str__(self):
        if self.completion == True:
            return f"{self.name} (Category: {self.category}, Priority: {self.level}) - ✓"
        else:
            return f"{self.name} (Category: {self.category}, Priority: {self.level}) - ✗"


class TaskList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        """Adds a task to the list."""
        self.tasks.append(task)

    def count_incomplete(self):
        """Return count of incomplete tasks."""
        count = 0 
        for task in self.tasks: 
            if task.completion == False:
                count +=1 
        return count 

    def filter_by_priority(self, level):
        """Return tasks with the specified priority level."""
        return [task for task in self.tasks if task.level == level]
    
    def display(self):        
        """Displays all tasks in the list."""
        print("Task List:")
        for task in self.tasks:
            print(task)
    
    def __str__(self):
        """Displays the task list."""
        return f"Task List: {len(self.tasks)} tasks, {self.count_incomplete()} incomplete"

# ---Main Flow ---
if __name__ == "__main__":
    my_list = TaskList()
    add_more = "yes"

    while add_more == "yes":
        name = input("Task name: ")
        category = input("Category: ")
        level = input("Priority (low/medium/high): ")
        task = Task(name, category, level)
        my_list.add_task(task) 
        add_more = input("Add another task? yes/no: ").lower().strip() 

    #Mark a task as complete
    mark = input("Which task would you like to mark as complete? (Enter task name): ")
    for task in my_list.tasks:
        if task.name == mark:
            task.mark_complete()
            print(f"Marked '{task.name}' as complete.")
            break
    else:
        print("Task not found.")

    #filter by priority
    priority_filter = input("Filter tasks by priority (low/medium/high): ")
    filtered_tasks = my_list.filter_by_priority(priority_filter)
    print(f"Tasks with {priority_filter} priority:")
    for task in filtered_tasks:
        print(task)
    if not filtered_tasks:
        print("No tasks found with that priority level.")

    #Display the updated task list
    my_list.display()
    print(f"Incomplete tasks: {my_list.count_incomplete()}")

        