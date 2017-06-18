class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age
    def __repr__(self):
        return repr((self.name, self.grade, self.age))


s = Student("a","A", 12)

# only input s in python cmd-line
# It will show ('a', 'A', 12)
