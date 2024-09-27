tuple1 = ()

tuple1 = tuple1 + (1, 2, 4, 7, 10)

# Sorting
list(tuple1).sort()
print(tuple1)

# Accesssing
print(tuple1[1])

# Slicing
print(tuple1[1:3])

# Length
print(len(tuple1))

# Maximum and minimum
print(max(tuple1))
print(min(tuple1))

# Type
print(type(tuple1))
print(isinstance(tuple1, tuple))

# Delete
del  tuple1

# Sets
sets1 = {1,4,7,9,10}

# Adding
sets1.add(5)
print(sets1)

# Remove
sets1.remove(1)
print(sets1)

# Remove from last
sets1.pop()
print(sets1)

# Length
print(len(sets1))

# Sorted
print(sorted(sets1))

# Sum
print(sum(sets1))

# Clear the set
sets1.clear()
print(sets1)


# Dictionary

dict1 = {1: "Jan", 2: "Feb", 3: "March"}

# To access the value using key
print(dict1[1])

# Traversing
for key in (dict1):
    print(f"{key} : {dict1[key]}")

# Updation
dict1.update({3: "April"})

# Deletion
del dict1[3]

# To get keys
print(dict1.keys())

# To get value of the dictionary
print(dict1.values())

# To get the key and value pair of dictionary
print(dict1.items())

# To empty the dictionary
print(dict1.clear())