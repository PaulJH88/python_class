class Employee:
    def __init__(self, name, job, age, hard_worker):
        self.name = name
        self.job = job
        self.age = age
        self.hard_worker = hard_worker

    def show_info(self):
        print("Name:", self.name)
        print("Job:", self.job)
        print("Age:", self.age)
        print("Hard Worker?", self.hard_worker)
        print("")

emp1 = Employee("Bob Johnson", "Python Engineer", 42, False)
emp2 = Employee("John Bobson", "Unpaid Intern", 18, True)

emp1.show_info()
emp2.show_info()

emp1.job = "Unemployed"
emp2.job = "Python Engineer"

emp1.show_info()
emp2.show_info()


