from rich.console import Console
from rich.progress import BarColumn, Progress

console = Console()

data = {"A": 10, "B": 30, "C": 50, "D": 40}
max_value = max(data.values())

sumi = sum(data.values())
with Progress(
    "{task.description}: ",
    BarColumn(),
    "{task.completed} of {task.total}",
    console=console
) as progress:
    for category, value in data.items():
        # Add a task for each category
        task_id = progress.add_task(f"{category}", total=sumi)
        # Update the task's progress
        progress.update(task_id, completed=value)
