#!/bin/python

class College:
    def __init__(self):
        self.staff_data = {
            "director": {"name": "John", "age": 23},
            "dean": {"name": "Doe", "age": 45},
            "exam officer": {"name": "Kamal", "age": 33}
        }
        self.staff_duties = {
            "director": ["manager departs", "head of staff", "decision maker"],
            "dean": ["coordinator", "head of faculties", "supervisor"],
            "exam officer": ["organize exams", "prepare results", "exam evaluator"]
        }

    def staff_info(self, roll):
        return self.staff_data.get(roll, "Staff not found")

    def staff_duty(self, roll):
        return self.staff_duties.get(roll, "Staff not found")

    def display(self, roll):
        staff_info = self.staff_info(roll)
        staff_duties = self.staff_duty(roll)

        if staff_info != "Staff not found":
            print(f"Information about {staff_info['name']} staff")
            for key, value in staff_info.items():
                print(f"{key}: {value}")

            print("\nDuties:")
            for duty in staff_duties:
                print(duty)
        else:
            print("Staff not found.")

    def append_new_staff(self, name, age, roll, duties):
        if roll not in self.staff_data:
            self.staff_data[roll] = {"name": name, "age": age}
            self.staff_duties[roll] = duties
            return "New record has been successfully added!"
        else:
            return "Staff role already exists!"

# Create a College instance
college = College()

name = input("Enter staff name: ")
roll = input(f"Enter {name} Roll: ")
age = int(input("Enter a staff Age: "))
n = int(input(f"Enter how many Duties {name} has?: "))
duties = []

for i in range(1, n + 1):
    duty = input(f"Enter Duty {i}: ")
    duties.append(duty)

result = college.append_new_staff(name, age, roll, duties)

print("")
choice = input("Do you want to see the new records? (y/n): ").lower()
if choice in ['y', 'yes', 'yep']:
    college.display(roll)
else:
    print(result)
"""
python do not provide data hiding like C++/JAVA etc, instead it use double under score
to indicate that a certain attribute or method is private eg __Method() __data01,
POLICY PYTHON WORKS ON
    Python does provide data hiding using a single underscore as a convention.
    Double underscores in Python trigger name mangling, not make attributes entirely private.
    The actual name used for name mangling is _ClassName__value.
    Python trusts developers to use code responsibly.

Name mangling is a technique in Python that alters the name of an attribute or method in a class 
to make it less likely to collide with names in subclasses
Note: In Python, when you prefix an attribute or method name with a double underscore (e.g., __value), 
Python internally changes the name of that attribute by adding the name of the class as a prefix. 
This is done to prevent accidental overriding of attributes or methods in subclasses. 
The actual name used for name mangling is _ClassName__value.
For example, if you have a class named MyClass with an attribute __value, 
it will be stored as _MyClass__value. This makes it less likely to clash with 
attributes of the same name in subclasses and provides a way to achieve a degree of encapsulation or privacy for class internals.'

"""