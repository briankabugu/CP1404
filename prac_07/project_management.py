"""
Project Management
Estimate: 60 minutes
Actual:   115 minutes
"""
from project import Project

def load_projects(filename):
    projects = []
    in_file = open(filename, "r")
    in_file.readline()
    for line in in_file:
        data = line.strip().split("\t")
        projects.append(Project(data[0], data[1], int(data[2]), float(data[3]), int(data[4])))
    return projects

def save_projects(filename, projects):
    out_file = open(filename, "w")
    out_file.write("Name\tStart Date\tPriority\tEstimate\tCompletion\n")
    for project in projects:
        out_file.write(f"{project.name}\t{project.start_date}\t{project.priority}\t{project.estimate}\t{project.completion}\n")

def display_projects(projects):
    completed_projects = []
    incomplete_projects = []
    for project in projects:
        if project.completion == 100:
            completed_projects.append(project)
        else:
            incomplete_projects.append(project)
    print("Completed projects:")
    completed_projects.sort()
    for project in completed_projects:
        print(project)
    print("Incompleted projects:")
    incomplete_projects.sort()
    incomplete_projects.reverse()
    for project in incomplete_projects:
        print(project)

def filter_projects_by_date(projects, date):
    filtered_projects = [project for project in projects if project.start_date_after(date)]
    display_projects(filtered_projects)

def add_new_project(projects):
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yyyy): ")
    priority = int(input("Priority: "))
    estimate = float(input("Cost estimate: $"))
    completion = int(input("Percent complete: "))
    projects.append(Project(name, start_date, priority, estimate, completion))

def update_project(projects):
    display_projects(projects)
    choice = int(input("Project choice: "))
    project = projects[choice]
    completion = input("New percentage complete: ")
    if completion:
        project.update_completion(int(completion))
    priority = input("New priority: ")
    if priority:
        project.update_priority(int(priority))

def main():
    print("Welcome to Pythonic Project Management")
    projects = load_projects("projects.txt")
    print(f"Loaded {len(projects)} projects from projects.txt")
    
    print("\nMenu:")
    print("- (L)oad projects")
    print("- (S)ave projects")
    print("- (D)isplay projects")
    print("- (F)ilter projects by date")
    print("- (A)dd new project")
    print("- (U)pdate project")
    print("- (Q)uit")
    choice = input(">>> ").strip().lower()
    
    while choice != 'q': 
        if choice == 'l':
            filename = input("Enter filename to load projects from: ")
            projects = load_projects(filename)
            print(f"Loaded {len(projects)} projects from {filename}")
        elif choice == 's':
            filename = input("Enter filename to save projects to: ")
            save_projects(filename, projects)
            print(f"Saved {len(projects)} projects to {filename}")
        elif choice == 'd':
            display_projects(projects)
        elif choice == 'f':
            date = input("Show projects that start after date (dd/mm/yyyy): ")
            filter_projects_by_date(projects, date)
        elif choice == 'a':
            add_new_project(projects)
        elif choice == 'u':
            update_project(projects)
        else:
            print("Invalid choice. Please try again.")
        choice = input(">>> ").strip().lower()
            

    save_choice = input("Would you like to save to projects.txt? ").strip().lower()
    if save_choice.startswith('y'):
        save_projects("projects.txt", projects)
        print(f"Saved {len(projects)} projects to projects.txt")
    print("Thank you for using custom-built project management software.")


main()
