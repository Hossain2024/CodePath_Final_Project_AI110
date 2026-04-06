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

The scheduler considers these contrains:
- Available time: The total amount of time the owner has for pet care in a day. Tasks are only added if they fit within this limit.
- Task duration: Each task has a time requirement, which affects whether it can be included in the schedule.
- Task frequency: Only tasks marked as "daily" are considered when generating the daily schedule.
- Completion status: Incomplete tasks are prioritized over completed ones to ensure essential care is not missed.
**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?

- I used AI to refactor some of the code & bransorm ideas
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
    - one time i didn't use AI as is when the AI generated UML diagram . I changes some of the things and asked for explanation before proceeding 
- How did you evaluate or verify what the AI suggested?
    - I evaluated AI sugestion based on my vision and my knowledge of UML 
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

- I was most satisfied with the UML diagram because it made it easier stay organized during my implementation
**b. What you would improve**

if i had another itteration I would add is support for multiple pets in the same schedule, allowing the owner to see and manage tasks for all their pets at once. This would make the app more practical for users with more than one pet and improve overall usability

**c. Key takeaway**

One important thing I learned from this project is the importance of evaluating AI-generated solutions critically. AI can help quickly generate ideas or boilerplate code, but it is essential to review, test, and adapt these suggestions to fit the specific requirements of the system. This process reinforced my understanding of designing systems thoughtfully and making tradeoffs between simplicity, usability, and functionality. 