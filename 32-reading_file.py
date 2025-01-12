import os
try:
  path="hello.txt"
  with open(path) as file:
    print(file.read())
    print("File exists and was read successfully.")
    pass
except IOError as error:
  print("Error:{error}".format(error=error))
  print("Unable to open file")
except Exception as error:
  print("Error:{error}".format(error=error))
  print('Something went wrong')

  