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
- Task: stores a tasks's name, category, and priority level, and completion status. Includes mark_complete() and __str__().
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
            return f"{self.name} (Category: {self.category}, Priority: {self.level})  ✓"
        else:
            return f"{self.name} (Category: {self.category}, Priority: {self.level})  ✗"


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
        filtered_tasks = []
        for task in self.tasks:
            if task.level.lower() == level.lower():
                filtered_tasks.append(task)
        return filtered_tasks
    
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
        name = input("Task name: ").lower().strip()
        while name == "":
            print("Task name cannot be empty. Please enter a valid task name.")
            name = input("Task name: ").lower().strip()
        category = input("Category: ").lower().strip()
        while category == "":
            print("Category cannot be empty. Please enter a valid category.")
            category = input("Category: ").lower().strip()
        level = input("Priority (low/medium/high): ").lower().strip()
        while level not in ["low", "medium", "high"]:
            print("Invalid priority level. Please enter low, medium, or high.")
            level = input("Priority (low/medium/high): ").lower().strip()
        task = Task(name, category, level)
        my_list.add_task(task) 
        # Mark a task as complete
        mark = input("Would you like to mark this task as completed yes/no: ").lower().strip()
        while mark not in ["yes", "no"]:
            print("Invalid input. Please enter yes or no.")
            mark = input("Would you like to mark this task as completed yes/no: ").lower().strip()
        if mark == "yes":
            task.mark_complete()
        add_more = input("Add another task? yes/no: ").lower().strip() 
        while add_more not in ["yes", "no"]:
            print("Invalid input. Please enter yes or no.")
            add_more = input("Add another task? yes/no: ").lower().strip()

    #filter by priority
    priority_filter = input("Filter tasks by priority (low/medium/high): ").lower().strip()
    while priority_filter not in ["low", "medium", "high"]:
        print("Invalid priority level. Please enter low, medium, or high.")
        priority_filter = input("Filter tasks by priority (low/medium/high): ").lower().strip()
    filtered_tasks = my_list.filter_by_priority(priority_filter)
    print(f"Tasks with {priority_filter} priority:")
    for task in filtered_tasks:
        print(task)
    if not filtered_tasks:
        print("No tasks found with that priority level.")

    #Display the updated task list
    my_list.display()
    print(f"Incomplete tasks: {my_list.count_incomplete()}")
