# Create a numeric variable
numFloat = 1.1

# Create a string variable
strName = "Igor Kolodiazhnyi"

# Compare numFloat's type with strName's type.
# Convert numFloat in string
print("Types match" if type(numFloat) == type(strName) else "Types don't match")
numFloat = str(numFloat)
print("New numFloat type is", type(numFloat))

# Create the fruits list
listFruits = ['Lime', 'Kiwi', 'Fig', 'Papaya', 'Mango']
print('Fruits list (initial state):', listFruits)

# Add an element into the end of the list.
# Add an element into the list by index.
listFruits.append('Tomato')
print('Fruits list (added in the end \'Tomato\'):', listFruits)
listFruits.insert(3, 'Apple')
print('Fruits list (added \'Apple\' by index 3)', listFruits)

# Delete the first element of the list (remove).
# Delete an element from the list by index (pop).
# Actually both operations could be done with pop method
listFruits.remove(listFruits[0])
print('Fruit list (removed the first element)', listFruits)
listFruits.pop(5)
print('Fruit list (removed the element with index 5)', listFruits)

# Reverse the list
listFruits.reverse()
print('Reversed fruit list:', listFruits)

# Print number of elements in the list
print('Number of elements in the fruit list:', len(listFruits))

# Make a list copy.
# Found the info that list.copy method doesn't work both in python 2.x and python 3.x.
# I've got the message "'list' object has no attribute 'copy'"
listFruitsCopy = list(listFruits)
print('Fruit list copy:', listFruitsCopy)


# Sort a list with a sorting algorithm (quick sort)
def quickSort(arr):
    # The base case when array consists 0 or 1 element
    if len(arr) < 2:
        return arr
    else:
        # The recursive case
        pivot = arr[0]
        # The subarray with elements less or equal pivot
        lower = [i for i in arr[1:] if i <= pivot]
        # The subarray with elemetns greater pivot
        higher = [i for i in arr[1:] if i > pivot]

        return quickSort(lower) + [pivot] + quickSort(higher)


print('Sorted fruit list (quick sort):', quickSort(listFruits))

# Sort a list with basic sorting algorithm
listFruitsCopy.sort()
print('Sorted copied fruit list (sorted())', listFruitsCopy)

# Create a list with unique words of provided string
strLine = "This is a test string for Internship Onix for python"
# First, make a list out of a string. Then find unique values
listUnique = list(set(strLine.split()))
print('List with unique values of provided string', listUnique)

# Sort a list alphabetically in a reverse order
listUnique = sorted(listUnique, key=str.lower, reverse=True)
print('Unique list sorted alphabetically in a reverse order', listUnique)

# Create a dictionary
dictTaskDiff = {1: "Easy",
                3: "Hard",
                2: "Medium"}
print("Created the task difficulties dictionary:", dictTaskDiff)

# Add an element into dictionary, get a value from the dict by a key, delete an element,
# get all keys, get all values.
dictTaskDiff[4] = "God like"
print("Added new element into dictionary:", dictTaskDiff)
print("Got value by key:", dictTaskDiff[1])
dictTaskDiff.pop(4)
print("Deleted an element from dictionary:", dictTaskDiff)
print("Get all keys: ", dictTaskDiff.keys())
print("Get all values: ", dictTaskDiff.values())


# Sort dict by keys
def sortDictByKeys(dictSourse):
    # Create new dict
    dictRes = {}
    # Fill in new dict with sorted key and value
    for key, value in sorted(dictTaskDiff.items()):
        dictRes.update({key: value})

    return dictRes


dictTaskDiff = sortDictByKeys(dictTaskDiff)
print("Dict is sorted by keys:", dictTaskDiff)


# Sort dict by values
def sortDictByValues(dictSourse):
    # Create new dict
    dictRes = {}

    for key, value in sorted(dictTaskDiff.items(), key=lambda x: x[1]):
        dictRes.update({key: value})

    return dictRes


dictTaskDiff = sortDictByValues(dictTaskDiff)
print("Dict is sorted by values:", dictTaskDiff)
