# **************************** Part 5 ***************************
# 5.1


def task_manager():
    tasks = {}

    def add_task(task_name: str, task_status="incomplete"):
        tasks[task_name] = task_status

    def get_tasks():
        return tasks

    def complete_task(task_name: str):
        if task_name in tasks:
            tasks[task_name] = "complete"
        else:
            print(f"Task {task_name} not found")

    return {
        "add_task": add_task,
        "get_tasks": get_tasks,
        "complete_task": complete_task,
    }
