# Index operator is used to access the elements of a list or a string.
# Index operator is used to access the elements of a dictionary using the key.
# Index operator is used to access the elements of a tuple.
# Index operator is not used to access the elements of a set.

name ="Opiyo Oscar"
last_name="";
for letter in name:
  if(letter==" "):
    break
  last_name+=letter
print("Last name:",last_name.upper())

students=["Oscar","Mark","Steve"]
print("First student:",students[0])
students.append("James")
print("Students after appending:",students)

# tuples of students
student=("Oscar",23,"Makerere University")
print("Student Name:",student[0])
# dictionary of students
student_grades={"Oscar":90,"Mark":80,"Steve":70}
print("Oscar's grade:",student_grades.get("Oscar"))

# set of students
students={"Oscar","Mark","Steve"}
teachers={"James","John","Mark"}
print("Students:",students)
print("Teachers:",teachers)

# set operations
# Union of sets
union_set = students.union(teachers)
print("Union of students and teachers:", union_set)

# Intersection of sets
intersection_set = students.intersection(teachers)
print("Intersection of students and teachers:", intersection_set)

# Difference of sets
difference_set = students.difference(teachers)
print("Difference of students and teachers:", difference_set)

# Symmetric difference of sets
symmetric_difference_set = students.symmetric_difference(teachers)
print("Symmetric difference of students and teachers:", symmetric_difference_set)

# Checking subset
is_subset = students.issubset(teachers)
print("Is students a subset of teachers?", is_subset)

# Checking superset
is_superset = students.issuperset(teachers)
print("Is students a superset of teachers?", is_superset)

# Checking disjoint sets
is_disjoint = students.isdisjoint(teachers)
print("Are students and teachers disjoint?", is_disjoint)

# Removing duplicates from a list using a set
my_list = [1, 2, 2, 3, 4, 4, 5]
unique_elements = set(my_list)
print("Unique elements from the list:", unique_elements)

# Removing duplicates from a list using a dictionary
my_list = [1, 2, 2, 3, 4, 4, 5]
unique_elements = list(dict.fromkeys(my_list))
print("Unique elements from the list:", unique_elements)

# Removing duplicates from a list using a set and a list comprehension
my_list = [1, 2, 2, 3, 4, 4, 5]
unique_elements = list(set(my_list))
print("Unique elements from the list:", unique_elements)

# Removing duplicates from a list using a dictionary and a list comprehension
my_list = [1, 2, 2, 3, 4, 4, 5]
unique_elements = list({element: None for element in my_list})
print("Unique elements from the list:", unique_elements)

# Removing duplicates from a list using a dictionary and a generator expression
my_list = [1, 2, 2, 3, 4, 4, 5]
unique_elements = list({element: None for element in my_list})
print("Unique elements from the list:", unique_elements)
# Output: Unique elements from the list: [1, 2, 3, 4, 5]

# Membership testing
print("Is 3 in students?", 3 in students)
print("Is 5 not in students?", 5 not in students)
# Output: Is 3 in students? False

# Output: Is 5 not in students? True

# Output: Last name: OPIYO
# Output: First student: Oscar

