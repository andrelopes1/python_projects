class Grade:
    minimum_passing = 65
    
    def __init__(self, score):
        self.score = score
    
    def is_passing(self):
        return self.score >= Grade.minimum_passing


class Student:
    def __init__(self, name, year):
        self.name = name
        self.year = year
        self.grades = []
        self.attendance = {}
    
    def add_grade(self, grade):
        if isinstance(grade, Grade):
            self.grades.append(grade)
    
    def get_average(self):
        if not self.grades:
            return 0
        return sum([grade.score for grade in self.grades]) / len(self.grades)


# Create three instances of the Student class
roger = Student("Roger van der Weyden", 10)
sandro = Student("Sandro Botticelli", 12)
pieter = Student("Pieter Bruegel the Elder", 8)

# Create a new Grade and add it to pieter's grades
grade_for_pieter = Grade(100)
pieter.add_grade(grade_for_pieter)

# Print whether Pieter's grade is passing and his average
print(pieter.grades[0].is_passing())  # True
print(pieter.get_average())  # 100
