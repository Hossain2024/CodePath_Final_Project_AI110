# 🐾 PawPal+ AI (Final Project)

PawPal+ AI is a Streamlit-based pet care assistant that helps owners plan and prioritize daily tasks for their pets using AI-style decision-making logic.

---

## Original Project (Module 2)

This project is an extension of my **PawPal+ (Module 2 Project)**, which focused on building a basic pet care scheduling system using Python and object-oriented programming.

The original system allowed users to create pets, assign tasks (such as feeding or walking), and generate a simple daily schedule based on available time. It demonstrated foundational OOP design and basic scheduling logic.

---

## Scenario

A busy pet owner needs help staying consistent with pet care. They want an assistant that can:

- Track pet care tasks (walks, feeding, medications, grooming, etc.)
- Consider constraints such as time availability and task importance
- Automatically generate a daily plan
- Explain why certain tasks were selected or skipped

PawPal+ AI extends this idea by acting as an intelligent assistant that makes scheduling decisions and explains its reasoning.

---

## What this system does

This system:

- Represents pet care tasks with duration and frequency
- Stores pets and owners using object-oriented design
- Generates a daily schedule based on time constraints
- Prioritizes tasks using AI-style logic
- Explains scheduling decisions in a transparent way

---

## Architecture Overview

The system is organized into modular components:

- **Owner**: Manages pets and aggregates all tasks  
- **Pet**: Stores pet information and associated tasks  
- **Task**: Represents individual care activities  
- **Scheduler**: Filters and prepares tasks  
- **AIPlanner**: Applies decision-making logic to prioritize and schedule tasks  
- **Streamlit UI**: Handles user interaction  

### Data Flow

User Input → Task Creation → Owner/Pet Storage → Scheduler → AIPlanner → Schedule + Explanation

---

## Setup

```bash
# Clone repository
git clone <your-repo-url>
cd <your-repo-folder>

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
### Demo
https://www.loom.com/share/ef55eebf4374420d9d41b1beec3342c3
