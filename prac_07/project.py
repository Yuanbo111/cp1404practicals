import datetime

class Project:
    """Represent a project with name, start date, priority, cost, and completion percentage."""
    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        """Initialize the project object"""
        self.name = name
        self.start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
        self.priority = int(priority)
        self.cost_estimate = float(cost_estimate)
        self.completion_percentage = int(completion_percentage)

    def __str__(self):
        """Return a formatted string representation of the project"""
        return (f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, "
                f"priority {self.priority}, estimate: ${self.cost_estimate:.2f}, "
                f"completion: {self.completion_percentage}%")