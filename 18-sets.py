# # Set=is a collection of unordered elements. It is a collection of unique elements.
# # Set is defined using curly braces {} and elements are separated by commas.
# # Set is mutable, but the elements of set are immutable.
# # Set is faster than list.
# # Set consumes less memory than list.
# # Set is used to store multiple items in a single variable.
# # Set does not support indexing.
# # Set does not support duplicate elements.
# # Set is used to perform mathematical operations like union, intersection, difference, and symmetric difference.
# # Set is used to remove duplicate elements from list.
# # Set is used to perform membership testing.
# # Creating a set
# my_set = {1, 2, 3, 4, 5}
# print("Original set:", my_set)

# # Adding elements to a set
# my_set.add(6)
# print("Set after adding an element:", my_set)

# # Adding multiple elements to a set
# my_set.update([7, 8, 9])
# print("Set after adding multiple elements:", my_set)

# # Removing an element from a set
# my_set.remove(1)  # Raises KeyError if the element is not present
# print("Set after removing an element:", my_set)

# # Discarding an element from a set
# my_set.discard(2)  # Does not raise an error if the element is not present
# print("Set after discarding an element:", my_set)

# # Popping an element from a set
# popped_element = my_set.pop()  # Removes and returns an arbitrary element
# print("Popped element:", popped_element)
# print("Set after popping an element:", my_set)

# # Clearing a set
# my_set.clear()
# print("Set after clearing all elements:", my_set)

# # Set operations
# set_a = {1, 2, 3, 4}
# set_b = {3, 4, 5, 6}

# # Union of sets
# union_set = set_a.union(set_b)
# print("Union of set_a and set_b:", union_set)

# # Intersection of sets
# intersection_set = set_a.intersection(set_b)
# print("Intersection of set_a and set_b:", intersection_set)

# # Difference of sets
# difference_set = set_a.difference(set_b)
# print("Difference of set_a and set_b:", difference_set)

# # Symmetric difference of sets
# symmetric_difference_set = set_a.symmetric_difference(set_b)
# print("Symmetric difference of set_a and set_b:", symmetric_difference_set)

# # Checking subset
# is_subset = set_a.issubset(set_b)
# print("Is set_a a subset of set_b?", is_subset)

# # Checking superset
# is_superset = set_a.issuperset(set_b)
# print("Is set_a a superset of set_b?", is_superset)

# # Checking disjoint sets
# is_disjoint = set_a.isdisjoint(set_b)
# print("Are set_a and set_b disjoint?", is_disjoint)

# # Removing duplicates from a list using a set
# my_list = [1, 2, 2, 3, 4, 4, 5]
# unique_elements = set(my_list)
# print("Unique elements from the list:", unique_elements)

# # Membership testing
# print("Is 3 in set_a?", 3 in set_a)
# print("Is 5 not in set_a?", 5 not in set_a)

teams={"Arsenal","Chelsea","Manchester United","Liverpool","Manchester City"}
teams.difference({"Players","Fans","Coaches","Managers"})
new_teams={"Barcelona","Real Madrid","Manchester United","Liverpool","Manchester City"}
teams.update(new_teams)
teams.add("Bayern Munich")
teams.remove("Chelsea")
teams.discard("Real Madrid")
# teams.clear()
copied_teams=teams.copy()
copied_teams.pop()
print("Poped element:",copied_teams.pop())
Inter_teams=teams.intersection(new_teams)
print("Intersection of teams and new_teams:",Inter_teams)
print()
team_union=teams.union(new_teams)
print("Is teams a subset of new_teams?",teams.issubset(new_teams))
print("Is teams a superset of new_teams?",teams.issuperset(new_teams))
print("Are teams and new_teams disjoint?",teams.isdisjoint(new_teams))
print("Difference of teams and new_teams:",teams.difference(new_teams))
print("Symmetric difference of teams and new_teams:",teams.symmetric_difference(new_teams))
print("Is Arsenal in teams?","Arsenal" in teams)
print("Union of teams and new_teams:",team_union)
for team in copied_teams:
  print(team)

