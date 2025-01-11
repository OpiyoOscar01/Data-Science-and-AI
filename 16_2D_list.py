#2D lists are considered as matrix.
# 2D list is a list of lists.
# 2D list is used to represent a matrix.
# 2D list is a list of lists.
matrix =[[1,2,3],
         [4,5,6],
         [7,8,9]]
print(matrix)
for  row in matrix:
  for  element in row:
    print(element,end=" ")
  print()
  
drinks=["coffee","tea","milk"]
vegetables=["carrot","cabbage","spinach"]
fruits=["banana","apple","mango"]
food=[drinks,vegetables,fruits]
print(food)
for category in food:
  for item in category:
    print(item,end=" ")
  print()