# str.format()-optional method that gives users more control when displaying output in python
animal="Cow"
planet="Moon"
print("The "+animal+" jumped over the "+planet)
# Better way
print("The {} jumped over the {}".format(animal,planet))
print("The {0} jumped over the {1}".format(animal,planet))# Using positional argument
print("The {1} jumped over the {1}".format(animal,planet))# Using positional argument
print("The {animal} jumped over the {planet}".format(animal="Dog",planet="Jupiter"))# Using keyword argument
print("The {animal} jumped over the {animal}".format(animal="Dog",planet="Jupiter"))# Using keyword argument

#Adding padding
print("Hello {name:<10},you are {age:>10} years old.You stay in {city:^10}".format(name="Oscar",age="23",city="Kampala"))# Using keyword argument

# formatting numbers
number =10006760
print("The number is {:.3f}".format(number))#3 decimal places
print("The number is {:e}".format(number))#scientific notation
print("The number is {:,}".format(number))#using thousand separator
print("The number is {:b}".format(number))#binary format
print("The number is {:x}".format(number))#hexadecimal format
print("The number is {:o}".format(number))#octal format





