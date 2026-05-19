class student():
    def __init__(self, name, age, dob,gender,grade):
        self.name = name
        self.age = age
        self.dob = dob
        self.gender=gender
        self.grade=grade


students = []
for i in range(0,2):
    print("Adding students")
    print(f"------Adding student {i} details-----------")
    name = input(f"Enter name of student :")
    age = input(f"Enter age of student:")
    dob = input(f"Enter date of birth: ")
    gender = input("Enter gender:")
    grade = input("Enter grade: ")
    obj = student(name,age,dob,gender,grade)
    students.append(obj)

for i  in range(len(students)):
    print(f"Student {i}")
    print("Name : ", students[i].name)
    print("Age : ", students[i].age)
    print("Dob : ", students[i].dob)
    print("Gender : ", students[i].gender)
    print("Grade : ", students[i].grade)

