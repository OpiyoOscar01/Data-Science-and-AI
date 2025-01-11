# List in python 3
# A list is a collection of items in a particular order. You can make a list that includes the letters of the alphabet, the digits from 0-9, or the names of all the people in your family.
# You can put anything you want into a list, and the items in your list don't have to be related in any particular way. Because a list usually contains more than one element, it's a good idea to make the name of your list plural, such as letters, digits, or names.
# In Python, square brackets ([]) indicate a list, and individual elements in the list are separated by commas.
teams=["Arsenal","Chelsea","Liverpool","Manchester United","Manchester City"]
print(teams)
print(teams[0])
print(teams[-1])
for team in teams:
  print(team)
# List operations
# Count the occurrences of "Chelsea" in the list and print the count
print(teams.count("Chelsea"))
print(teams.index("Chelsea"))

# Reverse the list and print it
teams.reverse()
print(teams)

# Sort the list and print it
teams.sort()
print(teams)
print(teams.append("Tottenham Hotspur"))
print(teams.insert(1,"Everton"))
print(teams.pop())
print(teams.remove("Chelsea"))
print(teams.clear())


