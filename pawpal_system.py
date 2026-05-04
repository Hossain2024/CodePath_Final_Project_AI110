from dataclasses import dataclass, field
from typing import List, Dict


# -------------------------
# Task
# -------------------------
@dataclass
class Task:
    description: str
    time: int  # duration in minutes
    frequency: str  # e.g., "daily", "weekly"
    completed: bool = False

    def mark_complete(self) -> None:
        """Mark the task as completed."""
        self.completed = True

    def mark_incomplete(self) -> None:
        """Mark the task as not completed."""
        self.completed = False


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
        """Add a task to this pet."""
        self.tasks.append(task)

    def remove_task(self, task: Task) -> None:
        """Remove a task from this pet."""
        if task in self.tasks:
            self.tasks.remove(task)

    def get_tasks(self) -> List[Task]:
        """Return all tasks for this pet."""
        return self.tasks


# -------------------------
# Owner
# -------------------------
class Owner:
    def __init__(self, name: str):
        self.name = name
        self.pets: List[Pet] = []

    def add_pet(self, pet: Pet) -> None:
        """Add a pet to the owner."""
        self.pets.append(pet)

    def remove_pet(self, pet: Pet) -> None:
        """Remove a pet."""
        if pet in self.pets:
            self.pets.remove(pet)

    def get_all_tasks(self) -> List[Task]:
        """Retrieve all tasks across all pets."""
        all_tasks = []
        for pet in self.pets:
            all_tasks.extend(pet.get_tasks())
        return all_tasks


# -------------------------
# Scheduler (Brain)
# -------------------------
class Scheduler:
    def __init__(self, owner: Owner):
        self.owner = owner

    def get_tasks_by_frequency(self, frequency: str) -> List[Task]:
        """Return tasks filtered by frequency (e.g., daily)."""
        return [
            task for task in self.owner.get_all_tasks()
            if task.frequency == frequency
        ]

    def get_pending_tasks(self) -> List[Task]:
        """Return all incomplete tasks."""
        return [
            task for task in self.owner.get_all_tasks()
            if not task.completed
        ]

    def get_completed_tasks(self) -> List[Task]:
        """Return all completed tasks."""
        return [
            task for task in self.owner.get_all_tasks()
            if task.completed
        ]

    def generate_daily_schedule(self, available_time: int) -> List[Task]:
        """
        Generate a simple daily plan:
        - Only includes 'daily' tasks
        - Prioritizes incomplete tasks
        - Stops when time runs out
        """
        schedule = []
        time_used = 0

        daily_tasks = self.get_tasks_by_frequency("daily")

        # Prioritize incomplete tasks first
        daily_tasks.sort(key=lambda t: t.completed)

        for task in daily_tasks:
            if time_used + task.time <= available_time:
                schedule.append(task)
                time_used += task.time

        return schedule

    def summarize_schedule(self, tasks: List[Task]) -> str:
        """Return a readable summary of the schedule."""
        if not tasks:
            return "No tasks scheduled."

        summary = []
        total_time = sum(task.time for task in tasks)

        summary.append(f"Total tasks: {len(tasks)}")
        summary.append(f"Total time: {total_time} minutes\n")

        for task in tasks:
            status = "Done" if task.completed else "Pending"
            summary.append(f"- {task.description} ({task.time} min) [{status}]")

        return "\n".join(summary)
# -------------------------
# AI PLANNER (Agent Layer)
# -------------------------
class AIPlanner:
    """
    This turns PawPal+ into an AI-style assistant.
    It decides what to do first, why, and what to skip.
    """

    def __init__(self, scheduler: Scheduler):
        self.scheduler = scheduler

    def prioritize_tasks(self, tasks: List[Task]) -> List[Task]:
        """
        AI-like prioritization:
        1. High priority first (we infer from completed + time urgency proxy)
        2. Short tasks first if tie (efficiency bias)
        """

        def score(task: Task):
            priority_score = 0

            # incomplete tasks are higher priority
            if not task.completed:
                priority_score += 2

            # shorter tasks slightly preferred (efficiency)
            priority_score += max(0, 100 - task.time)

            return priority_score

        return sorted(tasks, key=score, reverse=True)

    def generate_ai_schedule(self, available_time: int):
        """
        AI-driven scheduling:
        - Gets tasks
        - Prioritizes them
        - Builds optimized plan
        - Explains decisions
        """

        tasks = self.scheduler.get_tasks_by_frequency("daily")
        ordered_tasks = self.prioritize_tasks(tasks)

        schedule = []
        time_used = 0
        reasoning = []

        for task in ordered_tasks:
            if time_used + task.time <= available_time:
                schedule.append(task)
                time_used += task.time

                reasoning.append(
                    f"✔ Included '{task.description}' "
                    f"(priority decision: high relevance + fits time window)"
                )
            else:
                reasoning.append(
                    f"✖ Skipped '{task.description}' "
                    f"(not enough time left or lower priority)"
                )

        return schedule, reasoning

    def explain_plan(self, schedule: List[Task], reasoning: List[str]) -> str:
        """
        Converts AI decisions into human-readable explanation.
        """

        if not schedule:
            return "No tasks selected by AI planner."

        summary = []
        total_time = sum(t.time for t in schedule)

        summary.append("🧠 AI PLAN EXPLANATION\n")
        summary.append(f"Selected {len(schedule)} tasks")
        summary.append(f"Total time used: {total_time} minutes\n")

        summary.append("Decision Trace:")
        summary.extend(reasoning)

        return "\n".join(summary)