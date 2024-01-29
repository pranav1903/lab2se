import random
import nltk
from nltk.corpus import wordnet

def get_synonyms(word):
    synonyms = []
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            synonyms.append(lemma.name())
    return synonyms


class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary


employee1 = Employee(emp_id="161E90", name="Ramu", age=35, salary=59000)
employee2 = Employee(emp_id="171E22", name="Tejas", age=30, salary=82100)
employee3 = Employee(emp_id="171G55", name="Abhi", age=25, salary=100000)
employee4 = Employee(emp_id="151K46", name="Jaya", age=32, salary=85000)

print("Employee ID:", employee1.emp_id)
print("Name:", employee1.name)
print("Age:", employee1.age)
print("Salary (PM):", employee1.salary)

employees = [employee1, employee2, employee3, employee4]


print("press 1 to sort by age")
print("press 2 to sort by name")
print("press 3 to sort by salary")
x = int(input("enter here"))
if x == 1:
    sorted_employees = sorted(employees, key=lambda emp: emp.age)
elif x == 2:
    sorted_employees = sorted(employees, key=lambda emp: emp.name)
elif x == 3:
    sorted_employees = sorted(employees, key=lambda emp: emp.salary)
else:
    print("Invalid input")

# Print sorted employees
for emp in sorted_employees:
    print("Employee ID:", emp.emp_id)
    print("Name:", ' '.join(get_synonyms(emp.name, 1)[0].split('_')).capitalize())
    print("Age:", emp.age)
    print("Salary (PM):", emp.salary)
    print()