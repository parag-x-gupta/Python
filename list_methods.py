import sys

print("System version :" , sys.version)
print("Source python file path :", sys.executable)


my_list = [10,20,30,12,434,453,234,567,54,4323,43]

print("List is : ", my_list)

# .count() -> number of instancee of an element
# .insert() -> insert element at an index
# .sort()/.sorted() -> sorts the list
# .pop() -> remove element from the list
# .range() -> range object, iterable
# .len() -> length of the iterable


front_display_list = ["Mango", "Filet Mignon", "Chocolate Milk"]
print(front_display_list)

# Insert Method 
print(front_display_list.insert(0 ,"Pineapple")) # returns Nothing
print(front_display_list)

# Using pop method with index and without
data_science_topics = ["Machine Learning", "SQL", "Pandas", "Algorithms", "Statistics", "Python 3"]
print(data_science_topics)

# deleting the last element
data_science_topics.pop()
print(data_science_topics)

#deleting the second last element
data_science_topics.pop(-2)
print(data_science_topics)

# Range 
range_five_three = range(5, 15, 3)
range_diff_five = range(0, 40, 5)

# Using the count method
votes = ["Jake", "Jake", "Laurie", "Laurie", "Laurie", "Jake", 
"Jake", "Jake", "Laurie", "Cassie", "Cassie", "Jake", "Jake",
 "Cassie", "Laurie", "Cassie", "Jake", "Jake", "Cassie", "Laurie"]
print(votes)

votes_set = set(votes)
print(votes_set)

for element in votes_set:
  print(f"Total votes for {element} are : ", votes.count(element))

# Using the Sort method
addresses = ["221 B Baker St.", "42 Wallaby Way", "12 Grimmauld Place", "742 Evergreen Terrace", "1600 Pennsylvania Ave", "10 Downing St."]
addresses.sort()
print("Addresses are sort based on String ASCII values : ", addresses)

# Sorting Names
names = ["Ron", "Hermione", "Harry", "Albus", "Sirius"]
names.sort()


# Cities
cities = ["London", "Paris", "Rome", "Los Angeles", "New York", "Delhi", "Alberquerque"]
cities.sort(reverse = True)
print(cities)

# Using sorted method, always returns a new list and doesn't change the list inplace
