from pawpal_system import Owner, Pet, Task, Scheduler


def main():
    # Create Owner
    owner = Owner("Maliha")

    # Create Pets
    dog = Pet("Buddy", "Dog", 3)
    cat = Pet("Milo", "Cat", 2)

    # Add Tasks to Dog
    dog.add_task(Task("Morning Walk", 30, "daily"))
    dog.add_task(Task("Feed Dog", 10, "daily"))

    # Add Tasks to Cat
    cat.add_task(Task("Feed Cat", 5, "daily"))
    cat.add_task(Task("Clean Litter", 15, "daily"))

    # Add Pets to Owner
    owner.add_pet(dog)
    owner.add_pet(cat)

    # Create Scheduler
    scheduler = Scheduler(owner)

    # Generate Today's Schedule (e.g., 60 minutes available)
    todays_tasks = scheduler.generate_daily_schedule(60)

    # Print Schedule
    print("\n🐾 Today's Schedule:\n")

    if not todays_tasks:
        print("No tasks scheduled.")
    else:
        for task in todays_tasks:
            status = "Done" if task.completed else "Pending"
            print(f"- {task.description} ({task.time} min) [{status}]")

    # Optional: Print summary
    print("\nSummary:")
    print(scheduler.summarize_schedule(todays_tasks))


if __name__ == "__main__":
    main()