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

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
