class Student:
    def __init__(self, name_student,*subject):
        self.name = name_student
        self.subject = subject
        self.grade = []

    def add_grade(self, grade_student):
        if grade_student < 0 or grade_student >100:
            return "not allowed"
        else:
            self.grade.append(grade_student)

    def calculate_average(self):
        total = 0
        for grade in self.grade: ## == total = sum(self.grade)
            total += grade
        average1 = total / len(self.grade)
        return average1
    def print_info(self):
        print(f"name : {self.name}")
        print(f"subject : {self.subject}")
        print(f"grade : {self.grade}")
        print(f"average : {self.calculate_average()}")



s1 = Student("Ahmed", "Math","science")
s1.add_grade(5)
s1.print_info()
s1.add_grade(80)
s1.add_grade(90)
s1.add_grade(105)
s1.print_info()
