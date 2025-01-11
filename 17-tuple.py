# Tuple is contain ordered items which are interchangeable.
# Tuple is immutable, but the elements of tuple can be mutable.
# Tuple is defined using parentheses () and elements are separated by commas.
# Tuple is faster than list.
# Tuple consumes less memory than list.
# Tuple is used to store multiple items in a single variable.
student=("Oscar",23,"Makerere University")
print(student)
print(student[0])
print(student.count("Oscar"))
print(student.index("Oscar"))
for item in student:
  print(item)

# Tuple in list
students=[("Oscar",23,"Makerere University"),("Make",25,"Gulu University"),("Steve Okello",23,"Kyambogo University")]
print(students)
for student in students:
  for detail in student:
    print(detail,end=" ")
    
