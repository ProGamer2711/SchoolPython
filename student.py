class Student:
    def __init__(self, name: str, grades: dict[str, int]):
        self.name = name
        self.grades = grades

    def average_per_subject(self, subject: str):
        subjectGrades = self.grades[subject]
        return sum(subjectGrades) / len(subjectGrades)

    def average_grade(self):
        gradeTotal = 0
        gradeCount = 0

        for subjectGrades in self.grades.values():
            gradeTotal += sum(subjectGrades)
            gradeCount += len(subjectGrades)

        return gradeTotal / gradeCount


# Example
# ivan = Student("Ivan", {
#     "math": [4, 6, 6],
#     "english": [5, 5],
#     "bulgarian": [6, 6],
#     "history": [5, 4]
# })

# print(f"Ivan's average grade in math: {ivan.average_per_subject('math')}")
# print(f"Ivan's average grade: {ivan.average_grade()}")
