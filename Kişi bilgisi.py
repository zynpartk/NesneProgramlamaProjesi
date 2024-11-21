class Person:
    def _init_(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")


class Student(Person):
    def _init_(self, name, age, student_number):
        super()._init_(name, age)
        self.student_number = student_number

    def display_info(self):
        super().display_info()
        print(f"Student Number: {self.student_number}")


class Teacher(Person):
    def _init_(self, name, age, taught_subject):
        super()._init_(name, age)
        self.taught_subject = taught_subject

    def display_info(self):
        super().display_info()
        print(f"Teaches: {self.taught_subject}")


person = Person("Ahmet", 30)
student = Student("Zeynep", 20, 12345)
teacher = Teacher("Yasin", 40, "Matematik")


print("Person Info:")
person.display_info()

print("\nStudent Info:")
student.display_info()

print("\nTeacher Info:")
teacher.display_info()