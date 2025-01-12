# **kwargs:Used to unpack all parameter elements into a dictionary
def greetUser(**names):
  statement="Hello "
  for name,value in names.items():
    statement+=value+" "
  print(statement)

greetUser(title="Engineer",first_name="Oscar",last_name="Opiyo",middle_name="SoftDev",nick_name="Device")
greetUser(title="Engineer",first_name="Oscar")
greetUser(first_name="Oscar",last_name="Opiyo",middle_name="SoftDev")
    