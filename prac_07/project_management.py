
import datetime
from project import Project


def load_projects(file_path):
    """Load projects from a file."""
    projects = []
    try:
        with open(file_path, 'r') as file:
            next(file)
            for line in file:
                parts = line.strip().split('\t')
                name, start_date, priority, cost_estimate, completion_percentage = parts
                projects.append(Project(name, start_date, int(priority), float(cost_estimate), int(completion_percentage)))
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    return projects


def save_projects(file_path, projects):
    """Save projects to a file."""
    with open(file_path, 'w') as file:
        file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for project in projects:
            file.write(f"{project.name}\t{project.start_date}\t{project.priority}\t"
                       f"{project.cost_estimate:.2f}\t{project.completion_percentage}\n")


def display_projects(projects):
    """Display projects grouped by completion status."""
    incomplete_projects = [p for p in projects if p.completion_percentage < 100]
    completed_projects = [p for p in projects if p.completion_percentage == 100]

    print("\nIncomplete projects:")
    for project in sorted(incomplete_projects):
        print(project)

    print("\nCompleted projects:")
    for project in sorted(completed_projects):
        print(project)


def main():
    """Main function to manage projects."""
    file_path = "projects.txt"
    projects = load_projects(file_path)

    print("Welcome to Project Management")
    while True:
        print("\n(L)oad projects")
        print("(S)ave projects")
        print("(D)isplay projects")
        print("(A)dd new project")
        print("(Q)uit")
        choice = input(">>> ").lower()

        if choice == "l":
            projects = load_projects(file_path)
        elif choice == "s":
            save_projects(file_path, projects)
        elif choice == "d":
            display_projects(projects)
        elif choice == "a":
            name = input("Name: ")
            start_date = input("Start date (dd/mm/yyyy): ")
            priority = int(input("Priority: "))
            cost_estimate = float(input("Cost estimate: "))
            completion_percentage = int(input("Completion percentage: "))
            projects.append(Project(name, start_date, priority, cost_estimate, completion_percentage))
        elif choice == "q":
            save_projects(file_path, projects)
            print("Goodbye!")
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
