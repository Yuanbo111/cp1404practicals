"""
Project Management Program
Estimated time: 1 hour
Actual time:
"""

from project import Project
import datetime

FILENAME = "projects.txt"

def main():
    """Main function to run the project management program"""
    print("Welcome to Pythonic Project Management")
    projects = load_projects(FILENAME)
    print(f"Loaded {len(projects)} projects from {FILENAME}")
    MENU = "\n- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n" \
           "- (A)dd new project\n- (U)pdate project\n- (Q)uit"
    choice = ""
    while choice.lower() != "q":
        print(MENU)
        choice = input(">>> ").lower()
        if choice == "l":
            filename = input("Filename: ")
            projects = load_projects(filename)
        elif choice == "s":
            filename = input("Filename: ")
            save_projects(filename, projects)
        elif choice == "d":
            display_projects(projects)
        elif choice == "f":
            date_str = input("Show projects that start after date (dd/mm/yyyy): ")
            filter_projects_by_date(projects, date_str)
        elif choice == "a":
            projects.append(add_project())
        elif choice == "u":
            update_project(projects)
        elif choice == "q":
            save = input(f"Would you like to save to {FILENAME}? ").lower()
            if save in ["yes", "y"]:
                save_projects(FILENAME, projects)
            print("Thank you for using custom-built project management software.")

def load_projects(filename):
    """Load project data from the file"""
    projects = []
    with open(filename, "r") as in_file:
        next(in_file)  # Skip header
        for line in in_file:
            parts = line.strip().split("\t")
            if len(parts) == 5:
                name, start_time, priority, estimate, completion = parts
                project = Project(name, start_time, priority, estimate, completion)
                projects.append(project)
    return projects

def save_projects(filename, projects):
    """Save the list of Project objects"""
    with open(filename, "w") as out_file:
        out_file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for project in projects:
            out_file.write(f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t"
                           f"{project.priority}\t{project.cost_estimate}\t"
                           f"{project.completion_percentage}\n")

def display_projects(projects):
    """Display projects"""
    incomplete = []
    complete = []
    for project in projects:
        if project.is_complete():
            complete.append(project)
        else:
            incomplete.append(project)
    complete.sort()
    incomplete.sort()
    print("Incomplete projects:")
    for project in incomplete:
        print(f"{project}")
    print("Completed projects:")
    for project in complete:
        print(f"{project}")

def filter_projects_by_date(projects, date_str):
    """Filter and display projects that start after a given date, sorted by start date."""
    try:
        filter_date = datetime.datetime.strptime(date_str, "%d/%m/%Y").date()
    except ValueError:
        print("Invalid date format. Please use dd/mm/yyyy.")
        return

    # Filter projects starting after the given date
    filtered = []
    for project in projects:
        if project.start_date > filter_date:
            filtered.append(project)

    # Sort using a helper function instead of lambda
    def get_start_date(project):
        return project.start_date

    # Simple selection sort based on start_date (if sort key is restricted)
    for i in range(len(filtered) - 1):
        min_index = i
        for j in range(i + 1, len(filtered)):
            if get_start_date(filtered[j]) < get_start_date(filtered[min_index]):
                min_index = j
        if min_index != i:
            filtered[i], filtered[min_index] = filtered[min_index], filtered[i]

    # Display the sorted projects
    for project in filtered:
        print(project)

def add_project():
    """Prompt the user to input details for a new project and return a Project"""
    print("Let's add a new project")
    name = input("Name: ")
    start_date = get_valid_date("Start date (dd/mm/yyyy): ")
    priority = get_valid_int("Priority: ")
    estimate = get_valid_float("Cost estimate: $")
    completion = get_valid_int("Percent complete: ")
    return Project(name, start_date, priority, estimate, completion)


def get_valid_date(prompt):
    """Prompt the user for a valid date string in dd/mm/yyyy format"""
    while True:
        date_input = input(prompt)
        try:
            datetime.datetime.strptime(date_input, "%d/%m/%Y")
            return date_input
        except ValueError:
            print("Invalid date format. Please use dd/mm/yyyy.")


def get_valid_int(prompt):
    """Prompt the user for a valid integer"""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter an integer.")


def get_valid_float(prompt):
    """Prompt the user for a valid float"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

def update_project(projects):
    """Let the user update the completion percentage and/or priority of a selected project."""
    for i, project in enumerate(projects):
        print(f"{i} {project}")

    try:
        choice = int(input("Project choice: "))
        project = projects[choice]
    except (ValueError, IndexError):
        print("Invalid project choice.")
        return

    print(project)
    completion_input = input("New Percentage: ")
    if completion_input != "":
        try:
            project.completion_percentage = int(completion_input)
        except ValueError:
            print("Invalid completion percentage.")

    priority_input = input("New Priority: ")
    if priority_input != "":
        try:
            project.priority = int(priority_input)
        except ValueError:
            print("Invalid priority.")

if __name__ == "__main__":
    main()