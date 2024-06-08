#Write a Python program to check multiple keys exists in a dictionary

student = {
  'name': 'pammy',
  'age': 21,
  'city': 'Dhoraji'
}
print(student.keys() >= {'age', 'name'})
print(student.keys() >= {'City', 'pammy'})
print(student.keys() >= {'city', 'Dhoraji'})
