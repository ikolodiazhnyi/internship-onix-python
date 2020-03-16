# Copying list
from copy import copy

# Create a numeric variable
num_float = 1.1

# Create a string variable
str_name = "Igor Kolodiazhnyi"

# Compare num_float's type with str_name's type.
# Convert num_float in string
print("Types match" if type(num_float) == type(str_name) else "Types don't match")
num_float = str(num_float)
print("New num_float type is", type(num_float))

# Create the fruits list
list_fruits = ['Lime',
                'Kiwi',
                'Fig',
                'Papaya',
                'Mango']
print('Fruits list (initial state):', list_fruits)

# Add an element into the end of the list.
# Add an element into the list by index.
list_fruits.append('Tomato')
print('Fruits list (added in the end \'Tomato\'):', list_fruits)
list_fruits.insert(3, 'Apple')
print('Fruits list (added \'Apple\' by index 3)', list_fruits)

# Delete the first element of the list (remove).
# Delete an element from the list by index (pop).
# Actually both operations could be done with pop method
list_fruits.remove(list_fruits[0])
print('Fruit list (removed the first element)', list_fruits)
list_fruits.pop(5)
print('Fruit list (removed the element with index 5)', list_fruits)

# Reverse the list
list_fruits.reverse()
print('Reversed fruit list:', list_fruits)

# Print number of elements in the list
print('Number of elements in the fruit list:', len(list_fruits))

# Make a list copy
list_fruits_copy = copy(list_fruits)
print('Fruit list copy:', list_fruits_copy)

# Sort a list with a sorting algorithm (quick sort)
def quick_sort(arr):
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

        return quick_sort(lower) + [pivot] + quick_sort(higher)

print('Sorted fruit list (quick sort):', quick_sort(list_fruits))

# Sort a list with basic sorting algorithm
list_fruits_copy.sort()
print('Sorted copied fruit list (sorted())', list_fruits_copy)

# Create a list with unique words of provided string
str_line = "This is a test string for Internship Onix for python"
# First, make a list out of a string. Then find unique values
list_unique = list(set(str_line.split()))
print('List with unique values of provided string', list_unique)

# Sort a list alphabetically in a reverse order
list_unique = sorted(list_unique, key=str.lower, reverse=True)
print('Unique list sorted alphabetically in a reverse order', list_unique)

# Create a dictionary
dict_task_diff = {1: "Easy",
                  3: "Hard",
                  2: "Medium"}
print("Created the task difficulties dictionary:", dict_task_diff)

# Add an element into dictionary, get a value from the dict by a key, delete an element,
# get all keys, get all values.
dict_task_diff[4] = "God like"
print("Added new element into dictionary:", dict_task_diff)
print("Got value by key:", dict_task_diff[1])
dict_task_diff.pop(4)
print("Deleted an element from dictionary:", dict_task_diff)
print("Get all keys: ", dict_task_diff.keys())
print("Get all values: ", dict_task_diff.values())

# Sort dict by keys
def sort_dict_by_keys(dict_source):
    # Create new dict
    dict_res = {}
    # Fill in new dict with sorted key and value
    for key, value in sorted(dict_source.items()):
        dict_res.update({key: value})

    return dict_res

dict_task_diff = sort_dict_by_keys(dict_task_diff)
print("Dict is sorted by keys:", dict_task_diff)

# Sort dict by values
def sort_dict_by_values(dict_source):
    # Create new dict
    dict_res = {}

    for key, value in sorted(dict_source.items(), key=lambda x: x[1]):
        dict_res.update({key: value})

    return dict_res

dict_task_diff = sort_dict_by_values(dict_task_diff)
print("Dict is sorted by values:", dict_task_diff)