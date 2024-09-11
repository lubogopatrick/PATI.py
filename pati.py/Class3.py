class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def promote(self):
        self.grade += 1
        print(f"Promoted {self.name} to grade {self.grade}.")

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}")


# Usage
student = Student("John Doe", 15, 9)
student.display_info()
student.promote()
student.display_info()
```