#LAB PP Q4 b

class Person:
    def __init__(self, name, birthdate, city):
        self.name = name
        self.birthdate = birthdate
        self.city = city
    
class Student(Person):
    def __init__(self, name, birthdate, city, rollno, branch, totalMarks, year):
        self.rollno = rollno
        self.branch = branch
        self.totalMarks = totalMarks
        self.year = year
    
    def percentage(self):
        return self.totalMarks/5

class Grad(Student):
    def __init__(self, name, birthdate, city, rollno, branch, totalMarks, year, thesis):
        super().__init__(name, birthdate, city, rollno, branch, totalMarks, year)
        self.thesis = thesis

    def percentage(self):
        return self.totalMarks/6

class PostGrad(Student):
    def __init__(self, name, birthdate, city, rollno, branch, totalMarks, year, project):
        super().__init__(name, birthdate, city, rollno, branch, totalMarks, year)
        self.project = project

    def percentage(self):
        return self.totalMarks/4

grade = Grad("Rudra", "12/12/2000", "Kolkata", 123, "CSE", 500, 2020, "Thesis")
print(grade.percentage())

postGrad = PostGrad("Rudra", "12/12/2000", "Kolkata", 123, "CSE", 380, 2020, "Project")
print(postGrad.percentage())