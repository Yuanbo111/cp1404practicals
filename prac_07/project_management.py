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