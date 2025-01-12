import os
path="C:\\Users\\hp\\Desktop\\Course work.pdf"
if os.path.exists(path):
  if os.path.isfile(path):
    print("File exists")
  else:
    print("Directory exists")
else:
  print("Path does not exist")