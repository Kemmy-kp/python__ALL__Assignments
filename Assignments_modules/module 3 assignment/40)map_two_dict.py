#Write a Python program to map two lists into a dictionary




students = ['pammy', 'janvi', 'Priya']
marks = [89, 53, 92]

students_dict = dict(zip(students, marks))
print(students_dict)
