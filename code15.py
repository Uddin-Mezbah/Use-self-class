class Employee:
    no_of_leaves = 8

    def printdetails(self):
        return f"Name is {self.name}. Salary is {self.salary}and role is{self.role}"


ifaz = Employee()
pranto = Employee()

ifaz.name = "Ifaz"
ifaz.salary = "600$"
ifaz.role = "instructo"

pranto.name = "Pranto"
pranto.salary = "600$"
pranto.role = "jr excutive"

print(ifaz.printdetails())