# PawPal+ Project Reflection

## 1. System Design
1. Add and manage pet care tasks
    The user should be able to create, edit, and delete tasks related to their pet’s care, such as feeding, walking, administering medication, or grooming. Each task should include details like duration, priority, and whether it is mandatory.
2. Generate a daily care plan
    The user should be able to generate a daily schedule based on their available time and the list of tasks. The system should intelligently select tasks by prioritizing important and mandatory ones while respecting time constraints.
3. View the daily plan and explanation
    The user should be able to see a clear list of scheduled tasks for the day along with an explanation of why those tasks were selected (e.g., higher priority, mandatory tasks included first, time limitations).

**a. Initial design**

- Briefly describe your initial UML design.
    - My initial UML design for PawPal+ focused on representing the key entities and their relationships in a way that supports scheduling pet care tasks. The goal was to separate data storage (like tasks and pets) from logic (like planning the schedule), following clean object-oriented design principles.
- What classes did you include, and what responsibilities did you assign to each?
Task
    Responsibility: Represent a single pet care activity.
    Attributes: name, duration, priority, category, is_mandatory
    Methods: string representation
Pet
    Responsibility: Represent a pet and maintain a list of its tasks.
    Attributes: name, species, age, tasks
    Methods: add_task, remove_task, get_tasks
Owner
    Responsibility: Store owner information and available time for pet care.
    Attributes: name, available_time
    Methods: update_time
Schedule
    Responsibility: Store the selected tasks for a given day and calculate total scheduled time.
    Attributes: tasks
    Methods: add_task, calculate_time, get_tasks
Planner
    Responsibility: Generate a daily schedule based on task priority, mandatory tasks, and the owner's available time, and explain the reasoning.
    Methods: generate_plan, explain_plan
**b. Design changes**



---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

**b. Tradeoffs**

- Describe one tradeoff your sched