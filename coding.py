# Lists
my_list = [1, 2, 3, 4, 5]
print("Original List:", my_list)
print()
my_list.append(6)
print("List after appending:", my_list)
print()
my_list.insert(0, 0)
print("List after inserting:", my_list)
print()
my_list.remove(3)
print("List after removing:", my_list)
print()
popped_element = my_list.pop()
print("List after popping:", my_list, "Popped Element:", popped_element)
print()
print("Length of list:", len(my_list))
print()
my_list.sort()
print("Sorted list:", my_list)
print()
my_list.reverse()
print("Reversed list:", my_list)
print()
my_list2 = [7, 8, 9]
my_list.extend(my_list2)
print("List after extending:", my_list)
print()
sliced_list = my_list[2:5]
print("Sliced list:", sliced_list)
print()
my_list.clear()
print("List after clearing:", my_list)
print()

# Tuples
my_tuple = (10, 20, 30, 40, 50)
print("Original Tuple:", my_tuple)
print()
print("Tuple item at index 2:", my_tuple[2])
print()
print("Length of tuple:", len(my_tuple))
print()
sliced_tuple = my_tuple[1:4]
print("Sliced tuple:", sliced_tuple)
print()
concatenated_tuple = my_tuple + (60, 70)
print("Concatenated tuple:", concatenated_tuple)
print()
repeated_tuple = my_tuple * 2
print("Repeated tuple:", repeated_tuple)
print()
print("Is 30 in tuple?", 30 in my_tuple)
print()

# Sets
my_set = {1, 2, 3, 4, 5}
print("Original Set:", my_set)
print()
my_set.add(6)
print("Set after adding:", my_set)
print()
my_set.remove(3)
print("Set after removing:", my_set)
print()
my_set.discard(7)
print("Set after discarding (no error if not found):", my_set)
print()
my_set2 = {4, 5, 6, 7, 8}
union_set = my_set | my_set2
print("Union of sets:", union_set)
print()
intersection_set = my_set & my_set2
print("Intersection of sets:", intersection_set)
print()
difference_set = my_set - my_set2
print("Difference of sets:", difference_set)
print()
symmetric_difference_set = my_set ^ my_set2
print("Symmetric difference of sets:", symmetric_difference_set)
print()
my_set.clear()
print("Set after clearing:", my_set)
print()

# Dictionaries
my_dict = {"name": "John", "age": 30, "city": "New York"}
print("Original Dictionary:", my_dict)
print()
print("Value of 'name':", my_dict["name"])
print()
my_dict["age"] = 31
print("Dictionary after updating 'age':", my_dict)
print()
my_dict["occupation"] = "Engineer"
print("Dictionary after adding 'occupation':", my_dict)
print()
del my_dict["city"]
print("Dictionary after deleting 'city':", my_dict)
print()
print("Keys of dictionary:", my_dict.keys())
print()
print("Values of dictionary:", my_dict.values())
print()
print("Items of dictionary:", my_dict.items())
print()
print("Is 'name' in dictionary?", "name" in my_dict)
print()
print("Get value of 'age' (with default if not found):", my_dict.get("age", "N/A"))
print()
my_dict.clear()
print("Dictionary after clearing:", my_dict)
print()
# Combining Data Structures
list_of_tuples = [(1, 2), (3, 4), (5, 6)]
print("List of Tuples:", list_of_tuples)
print()
tuple_of_lists = ([1, 2], [3, 4], [5, 6])
print("Tuple of Lists:", tuple_of_lists)
print()
set_of_tuples = {(1, 2), (3, 4), (5, 6)}
print("Set of Tuples:", set_of_tuples)
print()
dict_of_lists = {"numbers": [1, 2, 3], "letters": ["a", "b", "c"]}
print("Dictionary of Lists:", dict_of_lists)
print()
list_of_dicts = [{"name": "Alice", "age": 25}, {"name": "Bob", "age": 30}]
print("List of Dictionaries:", list_of_dicts)
print()
dict_of_sets = {"set1": {1, 2, 3}, "set2": {4, 5, 6}}
print("Dictionary of Sets:", dict_of_sets)
print()
# More Dictionary Operations
another_dict = {"a": 1, "b": 2, "c": 3}
print("Another Dictionary:", another_dict)
print()
updated_dict = another_dict.copy()
updated_dict.update({"d": 4})
print("Updated Dictionary (using copy and update):", updated_dict)
print()
another_dict.setdefault("e", 5)
print("Dictionary after setdefault:", another_dict)
print()
popped_item = another_dict.pop("a")
print("Dictionary after popping 'a':", another_dict, "Popped Item:", popped_item)
print()
# More List Operations
another_list = [10, 20, 30, 40, 50]
print("Another List:", another_list)
print()
another_list.insert(2, 25)
print("List after inserting at index 2:", another_list)
print()
another_list.remove(40)
print("List after removing 40:", another_list)
print()
# More Set Operations
another_set = {10, 20, 30, 40, 50}
print("Another Set:", another_set)
print()
another_set.update({60, 70})
print("Set after updating with {60, 70}:", another_set)
print()
another_set.difference_update({10, 20})
print("Set after difference_update with {10, 20}:", another_set)
print()
# More Tuple Operations
another_tuple = (100, 200, 300, 400)
print("Another Tuple:", another_tuple)
print()
print("Index of 300 in tuple:", another_tuple.index(300))
print()
print("Count of 200 in tuple:", another_tuple.count(200))