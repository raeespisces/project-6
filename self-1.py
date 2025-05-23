class Student:
    def __init__(self, name, marks, school):
        self.name = name
        self.marks = marks
        self.school = school

    def display(self):
        print(f"Name: {self.name}, Marks: {self.marks}, School: {self.school} ")

if __name__ == "__main__":
    student1 = Student("Muhammad Raees", 95, "Lightstone")
    student1.display()
