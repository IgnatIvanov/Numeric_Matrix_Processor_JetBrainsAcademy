class Student:

    def __init__(self, name, last_name, birth_year):
        self.name = name
        self.last_name = last_name
        self.birth_year = birth_year
        # calculate the id here
        self.id = name[0] + last_name + str(birth_year)

in_name = input()
in_last_name = input()
in_birth_year = input()

student = Student(in_name, in_last_name, in_birth_year)
print(student.id)