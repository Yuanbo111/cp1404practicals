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