# task manager apps
from colorama import Fore
from time import sleep


class Task:
    def __init__(self, name, dueday, duration):
        self.name = name
        self.dueday = dueday
        self.duration = float(duration)
        self.completed = False
        self.dict = {
            "name": self.name,
            "dueday": self.dueday,
            "duration": self.duration,
            "completed": self.completed,
        }

    def __add__(self, other):
        return self.duration + float(other.duration)

    def __gt__(self, other):
        return True if self.duration > float(other.duration) else False

    def update(self, completed):
        if completed == True:
            self.completed = True
        else:
            pass

    def extend(self, extension):
        self.duration += float(extension)


class TaskApplication:
    def __init__(self):
        print(Fore.CYAN + "Welcome to taskIO")
        self.tasks = []

    def add(self):
        existsflag = False
        name = input("Please Enter the name of the task: ")
        dueday = input("Enter the due day for the task: ")
        duration = input("Enter the duration in hours of the task: ")

        for item in self.tasks:
            if item.name == name:
                existsflag = True
            else:
                existsflag = False

        if existsflag == True:
            print("A task with this name already exists!")
        else:
            newTask = Task(name, dueday, duration)
            self.tasks.append(newTask)

    def delete(self):
        name = input("Enter name of task to delete: ")

        for task in enumerate(self.tasks):
            if task[1].name == name:
                self.tasks.pop(task[0])
                found = True
                break
            else:
                found = False

        if found == False:
            print(Fore.RED + "No item found with this name")
        else:
            print(Fore.GREEN + "Item successfully deleted.")

    def display(self):
        print(Fore.YELLOW + "Your tasks for today :")
        sleep(1)

        print(Fore.LIGHTMAGENTA_EX + "Name --- DueDay --- Duration --- Completed?")

        for task in self.tasks:
            print(
                Fore.CYAN
                + f"{task.name} --- {task.dueday} --- {task.duration} --- {'Completed' if bool(task.completed) else 'Pending'}"
            )
            sleep(1)


# mainprogram

application = TaskApplication()

while True:
    decision = input(
        Fore.CYAN
        + "Press 1 to add a new task, 2 to delete a task, 3 to view all, anything else to exit"
    )
    if decision == "1":
        application.add()
    elif decision == "2":
        application.delete()
    elif decision == "3":
        application.display()
    else:
        print(Fore.RED + "Exiting")
        quit()
