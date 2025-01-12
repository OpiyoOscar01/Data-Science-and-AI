# dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# Dictionary is defined using curly braces {} and elements are separated by commas.
# Dictionary is mutable, but the elements of dictionary are immutable.
# Dictionary is faster than list.
# Dictionary consumes more memory than list.
# Dictionary is used to store multiple items in a single variable.
# Dictionary supports indexing.
# Dictionary does not support duplicate elements.
# Dictionary is used to perform membership testing.
# Dictionary is used to store key-value pairs.
# Dictionary is used to perform mathematical operations like union, intersection, difference, and symmetric difference.
# Dictionary is used to remove duplicate elements from list.
# Dictionary is used to perform membership testing.
# Creating a dictionary
my_dict = {"name": "Oscar", "age": 23, "university": "Makerere University"}
print("Original dictionary:", my_dict)
print("Name:", my_dict["name"])
print("Age:", my_dict.get("age"))
print("University:", my_dict.get("university"))
print("Keys:", my_dict.keys())
print("Values:", my_dict.values())
print("Items:", my_dict.items())

# Updating a dictionary
my_dict["age"] = 25
print("Dictionary after updating an element:", my_dict)

# Adding a new key-value pair
my_dict["location"] = "Kampala"

# Removing a key-value pair
my_dict.pop("location")
print("Dictionary after removing an element:", my_dict)

# Checking if a key exists in the dictionary
if "name" in my_dict:
    print("Key 'name' exists in the dictionary")
else:
    print("Key 'name' does not exist in the dictionary")

student_grades={"Oscar":90,"Mark":80,"Steve":70}
print("Student grades:",student_grades)
print("Oscar's grade:",student_grades.get("Oscar"))
student_grades["Oscar"]=95
student_grades.update({"James":85})
print("Student grades after updating:",student_grades)
for key,value in student_grades.items():
    print("Key:"+key+" Value:"+str(key
))