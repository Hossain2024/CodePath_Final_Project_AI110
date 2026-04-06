from dataclasses import dataclass, field
from typing import List


# -------------------------
# Task
# -------------------------
@dataclass
class Task:
    name: str
    duration: int
    priority: int
    category: str
    is_mandatory: bool = False

    def __str__(self) -> str:
        """Return a human-readable representation of the task."""
        pass


# -------------------------
# Pet
# -------------------------
@dataclass
class Pet:
    name: str
    species: str
    age: int
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        """Add a task to the pet."""
        pass

    def remove_task(self, task: Task) -> None:
        """Remove a task from the pet."""
        pass

    def get_tasks(self) -> List[Task]:
        """Return all tasks assigned to the pet."""
        pass


# -------------------------
# Owner
# -------------------------
class Owner:
    def __init__(self, name: str, available_time: int):
        self.name = name
        self.available_time = available_time

    def update_time(self, new_time: int) -> None:
        """Update the owner's available time."""
        pass


# -------------------------
# Schedule
# -------------------------
class Schedule:
    def __init__(self):
        self.tasks: List[Task] = []

    def add_task(self, task: Task) -> None:
        """Add a task to the schedule."""
        pass

    def calculate_time(self) -> int:
        """Return the total time of all scheduled tasks."""
        pass

    def get_tasks(self) -> List[Task]:
        """Return all scheduled tasks."""
        pass


# -------------------------
# Planner
# -------------------------
class Planner:
    def generate_plan(self, pet: Pet, owner: Owner) -> Schedule:
        """
        Generate a daily schedule based on:
        - task priority
        - mandatory tasks
        - available time
        """
        pass

    def explain_plan(self, schedule: Schedule, owner: Owner) -> str:
        """
        Return a human-readable explanation of why tasks were selected.
        """
        pass