######################################### 
#  ### List Tasks
######################################
# # 1. **Count Occurrences**: Given a list and an element, find how many times the element appears in the list.
# given_list=["a", "b", "c", "b", "g"]
# element="b"
# print(given_list.count(element))

# # 2. **Sum of Elements**: Given a list of numbers, calculate the total of all the elements.
# num_list=[1, 2, 4, 5, 6]
# print(sum(num_list))
# # 3. **Max Element**: From a given list, determine the largest element.
# given_list=["a", "b", "c", "b", "a"]
# print("Max Element:",  max(given_list))
# # 4. **Min Element**: From a given list, determine the smallest element.
# given_list=["a", "b", "c", "b", "a"]
# print("Min Element:",  min(given_list))
# # 5. **Check Element**: Given a list and an element, check if the element is present in the list.
# given_list=["a", "b", "c", "b", "g"]
# element="c"
# if element in given_list:
#     print("the element is present in the list")
# else:
#     print("the element is not present in the list")
# # 6. **First Element**: Access the first element of a list, considering what to return if the list is empty.
# given_list=["a", "b", "c", "b", "a"]
# first_e=given_list[0]
# if bool(first_e):
#     print(first_e)
# else:
#     print("list is empty")

# # 7. **Last Element**: Access the last element of a list, considering what to return if the list is empty.
# given_list=["a", "b", "c", "b", "a"]
# first_e=given_list[-1]
# if bool(first_e):
#     print(first_e)
# else:
#     print("list is empty")
# # 8. **Slice List**: Create a new list that contains only the first three elements of the original list.
# given_list=["a", "b", "c", "b", "a"]
# first_three=given_list[:3]
# print("new list", first_three)
# # 9. **Reverse List**: Create a new list that contains the elements of the original list in reverse order.
# given_list=["a", "b", "c", "b", "d"]
# reverce_list=given_list[::-1]
# print("reversed list", reverce_list)
# # 10. **Sort List**: Create a new list that contains the elements of the original list in sorted order.
# given_list=["a", "b", "c", "b", "d"]
# given_list.sort()
# print("sorted list", given_list)
# # 11. **Remove Duplicates**: Given a list, create a new list that contains only unique elements from the original list.
# given_list=["a", "b", "c", "b", "d"]
# print(list(set(given_list)))

# # 12. **Insert Element**: Given a list and an element, insert the element at a specified index.
# given_list=["a", "b", "c", "b", "d"]
# given_list.insert(2, "e")
# print(given_list)
# # 13. **Index of Element**: Given a list and an element, find the index of the first occurrence of the element.
# given_list=["a", "b", "c", "b", "g"]
# element="b"
# print(given_list.index(element))
# # 14. **Check for Empty List**: Determine if a list is empty and return a boolean.
# given_list=["a", "b", "c", "b", "g"]
# print(bool(given_list))
# # 15. **Count Even Numbers**: Given a list of integers, count how many of them are even.
# integer_list=[1,2,3,4,5,6,5,88]
# even_count=0
# odd_count=0
# for char in integer_list:
#     if char%2==0:
#         even_count +=1
#     else:
#         odd_count +=1

# print(even_count)
# # 16. **Count Odd Numbers**: Given a list of integers, count how many of them are odd.
# integer_list=[1,2,3,4,5,6,5,88]
# even_count=0
# odd_count=0
# for char in integer_list:
#     if char%2==0:
#         even_count +=1
#     else:
#         odd_count +=1

# print(odd_count)
# # 17. **Concatenate Lists**: Given two lists, create a new list that combines both lists.
# list1=[1,2,3,4,5,6,5,88]
# list2=["a", "b", "c", "b", "g"]
# list1.extend(list2)
# print(list1)
# # 18. **Find Sublist**: Given a list and a sublist, check if the sublist exists within the list.
# list1 = [1, 2, 3, 4, 5, 6, 5, 88]
# list2 = ["a", "b", "c", "b", "g"]

# if all(item in list1 for item in list2):
#     print("list2 is a sublist of list1")
# else:
#     print("list2 is not a sublist of list1")

# # 19. **Replace Element**: Given a list, replace the first occurrence of a specified element with another element.
# list1=[1,2,3,4,5,6,5,88]
# list1.index(5)
# list1[list1.index(5)]=10
# print(list1)
# # 20. **Find Second Largest**: From a given list, find the second largest element.
# list1=[1,2,3,4,5,6,5,88]
# a=list1.index(max(list1))
# list1.remove(list1[a])
# print(max(list1))
# # 21. **Find Second Smallest**: From a given list, find the second smallest element.
# list1=[1,2,3,4,5,6,5,88]
# a=list1.index(min(list1))
# list1.remove(list1[a])
# print(min(list1))
# # 22. **Filter Even Numbers**: Given a list of integers, create a new list that contains only the even numbers.
# integer_list=[1,2,3,4,5,6,5,88]
# even_count=[]
# odd_count=[]
# for char in integer_list:
#     if char%2==0:
#         even_count.append(char)
#     else:
#         odd_count.append(char)
# print(even_count)
# # 23. **Filter Odd Numbers**: Given a list of integers, create a new list that contains only the odd numbers.
# integer_list=[1,2,3,4,5,6,5,88]
# even_count=[]
# odd_count=[]
# for char in integer_list:
#     if char%2==0:
#         even_count.append(char)
#     else:
#         odd_count.append(char)
# print(odd_count)
# # 24. **List Length**: Determine the number of elements in the list.
# integer_list=[1,2,3,4,5,6,5,88]
# print(len(integer_list))
# # 25. **Create a Copy**: Create a new list that is a copy of the original list.
# integer_list=[1,2,3,4,5,6,5,88]
# new_list=integer_list.copy()
# print(new_list)
# # 26. **Get Middle Element**: Given a list, find the middle element. If the list has an even number of elements, return the two middle elements.
# integer_list=[1,2,3,4,5,6,5]
# if (len(integer_list)/2)%2==0:
#     print( integer_list[int((len(integer_list)/2)-1)], integer_list[int((len(integer_list)/2))])
# else:
#     print(integer_list[int((len(integer_list)/2))])
# # 27. **Find Maximum of Sublist**: Given a list, find the maximum element of a specified sublist.
# integer_list=[1,2,3,4,5,6,5,88]
# sublist=integer_list[2:6]
# print(max(sublist))
# # 28. **Find Minimum of Sublist**: Given a list, find the minimum element of a specified sublist.
# integer_list=[1,2,3,4,5,6,5,88]
# sublist=integer_list[2:6]
# print(min(sublist))
# # 29. **Remove Element by Index**: Given a list and an index, remove the element at that index if it exists.
# integer_list=[1,2,3,4,5,6,5,88]
# a=integer_list[3]
# integer_list.remove(a)
# print(integer_list)
# # 30. **Check if List is Sorted**: Determine if the list is sorted in ascending order and return a boolean.
# integer_list=[1,2,3,4,5,6,5,88]
# print(integer_list.sort()==integer_list)
# # 31. **Repeat Elements**: Given a list and a number, create a new list where each element is repeated that number of times.
# integer_list=[1,2,3,4,5,6,5,88]
# new=[]
# for char in integer_list:
#     new.extend([char]*char)
# print(new)
# # 32. **Merge and Sort**: Given two lists, create a new sorted list that merges both lists.
# list1=["a", "d", "c", "e", "g"]
# list2=["a", "b", "c", "b", "g"]
# list1.extend(list2)
# list1.sort()
# print(list1)

# # 33. **Find All Indices**: Given a list and an element, find all the indices of that element in the list.
# lst=['as', 'sd', 'sd']
# element='sd'
# indices = []
# for i in range(len(lst)):
#     if lst[i] == element:
#         indices.append(i)
# print(indices)

# # 34. **Rotate List**: Given a list, create a new list that is a rotated version of the original list (shift elements to the right).
# list1=["a", "d", "c", "e", "g"]
# merge=list(list1[-1]) + list1[0:-1]
# print(merge)

# # 35. **Create Range List**: Create a list of numbers in a specified range (e.g., from 1 to 10).
# list1=[]
# for i in range(1, 11):
#     list1.append(i)
# print(list1)

# # 36. **Sum of Positive Numbers**: Given a list of numbers, calculate the sum of all positive numbers.
# list_num=[13, 15, -3, -5]
# positive=[]
# for i in list_num:
#     if i>0:
#        positive.append(i)
# print(sum(positive))

# # 37. **Sum of Negative Numbers**: Given a list of numbers, calculate the sum of all negative numbers.
# list_num=[13, 15, -3, -5]
# negative=[]
# for i in list_num:
#     if i<0:
#        negative.append(i)
# print(sum(negative))
# # 38. **Check Palindrome**: Given a list, check if the list is a palindrome (reads the same forwards and backwards).
# list_num=[13, 15, -3, -5]
# print(list_num==list_num.reverse())
# # 39. **Create Nested List**: Create a new list that contains sublists, where each sublist contains a specified number of elements from the original list.
# original_list = [1, 2, 3, 4, 5, 6, 7, 8]
# n = 3
# nested_list = []

# for i in range(0, len(original_list), n):
#     nested_list.append(original_list[i:i+n])

# print(nested_list)

# # 40. **Get Unique Elements in Order**: Given a list, create a new list that contains unique elements while maintaining the original order.
# list_num = [13, 15, -3, -5, 13]
# ordered = list(dict.fromkeys(list_num))
# print(ordered)

#############################################
# ### Tuple Tasks
##############################################
# # 1. **Count Occurrences**: Given a tuple and an element, find how many times the element appears in the tuple.
# tuple1=('i', 'you', 'he', 'he', 'she')
# element='he'
# a=tuple1.count(element)
# print(a)
# # 2. **Max Element**: From a given tuple, determine the largest element.
# tuple1=('i', 'you', 'he', 'he', 'she')
# mx=max(tuple1)
# print(mx)
# # 3. **Min Element**: From a given tuple, determine the smallest element.
# tuple1=('i', 'you', 'he', 'he', 'she')
# mn=min(tuple1)
# print(mn)
# # 4. **Check Element**: Given a tuple and an element, check if the element is present in the tuple.
# tuple1=('i', 'you', 'he', 'he', 'she')
# element='he'
# print(element in tuple1)
# # 5. **First Element**: Access the first element of a tuple, considering what to return if the tuple is empty.
# tple1=('i', 'you', 'he', 'he', 'she')
# first_e=tple1[0]
# if bool(first_e):
#     print(first_e)
# else:
#     print("tuple is empty")
# # 6. **Last Element**: Access the last element of a tuple, considering what to return if the tuple is empty.
# tple1=('i', 'you', 'he', 'he', 'she')
# last_e=tple1[-1]
# if bool(last_e):
#     print(last_e)
# else:
#     print("tuple is empty")
# # 7. **Tuple Length**: Determine the number of elements in the tuple.
# tple1=('i', 'you', 'he', 'he', 'she')
# print(len(tple1))

# # 8. **Slice Tuple**: Create a new tuple that contains only the first three elements of the original tuple.
# tple1=('i', 'you', 'he', 'he', 'she')
# print(tple1[:3])
# # 9. **Concatenate Tuples**: Given two tuples, create a new tuple that combines both.
# tple1=('i', 'you', 'he', 'he', 'she')
# tple2=('we', 'you', 'they', 'it', 'it')
# merged= tple1 + tple2
# print(merged)
# # 10. **Check if Tuple is Empty**: Determine if a tuple has any elements.
# tple1=('i', 'you', 'he', 'he', 'she')
# print(bool(tple1))
# # 11. **Get All Indices of Element**: Given a tuple and an element, find all the indices of that element in the tuple.

# tple1=('i', 'you', 'he', 'he', 'she')
# element="he"
# indeses=[]
# for i in range(0, len(tple1)):
#     if tple1[i]==element:
#         indeses.append(i)
# print(indeses)

# # 12. **Find Second Largest**: From a given tuple, find the second largest element.
# tple1=('i', 'you', 'he', 'he', 'she')
# a=sorted(tuple(set(tple1)))
# print(a[len(a)-2])
# # 13. **Find Second Smallest**: From a given tuple, find the second smallest element.
# tple1=('i', 'you', 'he', 'he', 'she')
# a=sorted(tuple(set(tple1)))
# print(a[1])
# # 14. **Create a Single Element Tuple**: Create a tuple that contains a single specified element.
# single_tuple = (10,)
# print(single_tuple)
# print(type(single_tuple))

# # 15. **Convert List to Tuple**: Given a list, create a tuple containing the same elements.
# list1=['i', 'you', 'he', 'he', 'she']
# tuple1=tuple(list1)
# print(tuple1)
# # 16. **Check if Tuple is Sorted**: Determine if the tuple is sorted in ascending order and return a boolean.
# tple1=('i', 'you', 'he', 'he', 'she')
# print(tple1==sorted(tple1))
# # 17. **Find Maximum of Subtuple**: Given a tuple, find the maximum element of a specified subtuple.
# tple1=('i', 'you', 'he', 'he', 'she')
# sub_tp=tple1[3:5]
# print(max(sub_tp))
# # 18. **Find Minimum of Subtuple**: Given a tuple, find the minimum element of a specified subtuple.
# tple1=('i', 'you', 'he', 'he', 'she')
# sub_tp=tple1[3:5]
# print(min(sub_tp))
# # 19. **Remove Element by Value**: Given a tuple and an element, create a new tuple that removes the first occurrence of that element.
# tple1=('i', 'you', 'he', 'he', 'she')
# a=list(tple1)
# a.remove('he')
# print(tuple(a))
# # 20. **Create Nested Tuple**: Create a new tuple that contains subtuples, where each subtuple contains specified elements from the original tuple.
# tple1 = ('i', 'you', 'he', 'she')

# nested_tuple = tuple(
#     tple1[i:i+2] for i in range(0, len(tple1), 2)
# )

# print(nested_tuple)


# # 21. **Repeat Elements**: Given a tuple and a number, create a new tuple where each element is repeated that number of times.
# tple1 = ('i', 'you', 'he', 'she')
# n=5
# new=tuple(
#     [tple1[i]]*n for i in range(0, len(tple1))
# )
# print(new)
# # 22. **Create Range Tuple**: Create a tuple of numbers in a specified range (e.g., from 1 to 10).
# range_tuple = tuple(range(1, 11))
# print(range_tuple)

# # 23. **Reverse Tuple**: Create a new tuple that contains the elements of the original tuple in reverse order.
# tule1=()
# reversedtp=tule1[::-1]
# # 24. **Check Palindrome**: Given a tuple, check if the tuple is a palindrome (reads the same forwards and backwards).
# tule1=()
# reversedtp=tule1[::-1]
# print(tule1==reversedtp)
# # 25. **Get Unique Elements**: Given a tuple, create a new tuple that contains only the unique elements while maintaining the original order.
# tule1=(('i', 'you', 'he', 'he', 'she'))
# unitup=tuple(dict.fromkeys(tule1))
# print(unitup)

##############################################################
# ### Set Tasks
############################################################
# # 1. **Union of Sets**: Given two sets, create a new set that contains all unique elements from both sets.
# first_set={1, 5, 3, 8, 5, 2}
# second_set={'as', 'ad', 'big', 'ad', 'rg'}
# uni_element=first_set | second_set
# print(uni_element)
# # 2. **Intersection of Sets**: Given two sets, create a new set that contains elements common to both sets.
# first_set={1, 5, 3, 8, 5, 2}
# second_set={'as', 'ad', 'big', 'ad', 'rg', 8}
# intersection_elements=first_set & second_set
# print(intersection_elements)
# # 3. **Difference of Sets**: Given two sets, create a new set with elements from the first set that are not in the second.
# first_set={1, 5, 3, 8, 5, 2}
# second_set={'as', 'ad', 'big', 'ad', 'rg', 8}
# only_first_elements=first_set - second_set
# print(only_first_elements)
# # 4. **Check Subset**: Given two sets, check if one set is a subset of the other.
# first_set={1, 5, 3, 8, 5, 2}
# second_set={'as', 'ad', 'big', 'ad', 'rg', 8}
# print(second_set in first_set)
# # 5. **Check Element**: Given a set and an element, check if the element exists in the set.
# first_set={1, 5, 3, 8, 5, 2}
# element=5
# print(element in first_set)
# # 6. **Set Length**: Determine the number of unique elements in a set.
# first_set={1, 5, 3, 8, 5, 2}
# lenth=len(first_set)
# print(lenth)
# # 7. **Convert List to Set**: Given a list, create a new set that contains only the unique elements from that list.
# first_list=[1, 5, 3, 8, 5, 2]
# first_set=set(first_list)
# print(first_set)
# # 8. **Remove Element**: Given a set and an element, remove the element if it exists.
# first_set={1, 5, 3, 8, 5, 2}
# element=5
# first_set.discard(element)
# print(first_set)
# # 9. **Clear Set**: Create a new empty set from an existing set.
# first_set={1, 5, 3, 8, 5, 2}
# first_set.clear()
# print(first_set)
# # 10. **Check if Set is Empty**: Determine if a set has any elements.
# first_set={1, 5, 3, 8, 5, 2}

# print(bool(first_set))
# # 11. **Symmetric Difference**: Given two sets, create a new set that contains elements that are in either set but not in both.
# first_set={1, 5, 3, 8, 5, 2}
# second_set={'as', 'ad', 'big', 'ad', 'rg', 8}
# symmetric=first_set.symmetric_difference(second_set)
# print(symmetric)
# # 12. **Add Element**: Given a set and an element, add the element to the set if it is not already present.
# first_set={1, 5, 3, 8, 5, 2}
# first_set.add(4)
# print(first_set)
# # 13. **Pop Element**: Given a set, remove and return an arbitrary element from the set.
# first_set={1, 5, 3, 8, 5, 2}
# first_set.pop()
# print(first_set)
# # 14. **Find Maximum**: From a given set of numbers, find the maximum element.
# first_set={1, 5, 3, 8, 5, 2}

# print(max(first_set))
# # 15. **Find Minimum**: From a given set of numbers, find the minimum element.
# first_set={1, 5, 3, 8, 5, 2}

# print(min(first_set))
# # 16. **Filter Even Numbers**: Given a set of integers, create a new set that contains only the even numbers.
# first_set={1, 5, 3, 8, 5, 2}
# even_num=set() 
# for i in first_set:
#     if i%2==0:
#         even_num.add(i)
# print(even_num)

# # 17. **Filter Odd Numbers**: Given a set of integers, create a new set that contains only the odd numbers.
# first_set={1, 5, 3, 8, 5, 2}
# odd_num=set() 
# for i in first_set:
#     if i%2!=0:
#         odd_num.add(i)
# print(odd_num)
# # 18. **Create a Set of a Range**: Create a set of numbers in a specified range (e.g., from 1 to 10).
# range_set=set()
# for i in range(1, 11):
#     range_set.add(i)
# print(range_set)
# # 19. **Merge and Deduplicate**: Given two lists, create a new set that merges both lists and removes duplicates.
# first_set={1, 5, 3, 8, 5, 2}
# second_set={'as', 'ad', 'big', 'ad', 'rg'}
# uni_element=first_set | second_set
# print(uni_element)
# # 20. **Check Disjoint Sets**: Given two sets, check if they have no elements in common.
# first_set={1, 5, 3, 8, 5, 2}
# second_set={'as', 'ad', 'big', 'ad', 'rg'}
# com_element=first_set.isdisjoint(second_set)
# print(com_element)
# # 21. **Remove Duplicates from a List**: Given a list, create a set from it to remove duplicates, then convert back to a list.
# first_list=[1, 5, 3, 8, 5, 2]
# new_list=list(set(first_list))
# print(new_list)
# # 22. **Count Unique Elements**: Given a list, determine the count of unique elements using a set.
# first_list=[1, 5, 3, 8, 5, 2]
# new_list=list(set(first_list))
# print(len(new_list))
# # 23. **Generate Random Set**: Create a set with a specified number of random integers within a certain range.
# import random
# random_set=set()
# while len(random_set)<5:
#      random_set.add(random.randint(1,30))   
# print(random_set)


# random_set = set(random.sample(range(1, 21), 5))
# print(random_set)

############################################################
### Dictionary Tasks

# # 1. **Get Value**: Given a dictionary and a key, retrieve the associated value, considering what to return if the key doesn’t exist.
# people={'name':'Ali', 'age':23, 'work':'doctor'}
# key='age'
# if key in people:
#     print(people[key])
# else:
#     print("key does not exist in dict")
# # 2. **Check Key**: Given a dictionary and a key, check if the key is present in the dictionary.
# people={'name':'Ali', 'age':23, 'work':'doctor'}
# key='age'
# if key in people:
#     print("key  exists in dict")
# else:
#     print("key does not exist in dict")
# # 3. **Count Keys**: Determine the number of keys in the dictionary.
# people={'name':'Ali', 'age':23, 'work':'doctor'}
# s=len(people)
# print(s)
# # 4. **Get All Keys**: Create a list that contains all the keys in the dictionary.
# people={'name':'Ali', 'age':23, 'work':'doctor'}
# keys=list(people.keys())
# print(keys)
# # 5. **Get All Values**: Create a list that contains all the values in the dictionary.
# people={'name':'Ali', 'age':23, 'work':'doctor'}
# values=list(people.values())
# print(values)
# # 6. **Merge Dictionaries**: Given two dictionaries, create a new dictionary that combines both.
# people={'name':'Ali', 'age':23, 'work':'doctor'}
# teachers={'name':'Azamat', 'year':1999, 'job':'programmer'}
# people.update(teachers)
# print(people)
# # 7. **Remove Key**: Given a dictionary and a key, remove the key if it exists, handling the case if it doesn’t.
# people={'name':'Ali', 'age':23, 'work':'doctor'}
# key='name'
# if key in people:
#     people.pop(key)
#     print('key removed')
# else:
#     print('key does not exist')

# # 8. **Clear Dictionary**: Create a new empty dictionary.
# new={}
# # 9. **Check if Dictionary is Empty**: Determine if a dictionary has any elements.
# people={'name':'Ali', 'age':23, 'work':'doctor'}
# if bool(people)==False:
#     print('dict is empty')
# else:
#     print(people, "\n dict is not empty")
# # 10. **Get Key-Value Pair**: Given a dictionary and a key, retrieve the key-value pair if the key exists.
# people={'name':'Ali', 'age':23, 'work':'doctor'}
# key='name'
# if key in people:
#     print(key, people[key])
# else:
#     print("key not found")
# # 11. **Update Value**: Given a dictionary, update the value for a specified key.
# people={'name':'Ali', 'age':23, 'work':'doctor'}
# people["name"]='Azamat'
# print(people)
# # 12. **Count Value Occurrences**: Given a dictionary, count how many times a specific value appears across the keys.
# people={'name':'Ali', 'age':23, 'work':'doctor'}
# value=23
# count=sum(1 for i in people.values() if i==value)
# print(count)
# # 13. **Invert Dictionary**: Given a dictionary, create a new dictionary that swaps keys and values.
# people={'name':'Ali', 'age':23, 'work':'doctor'}

# new_dict={}
# for key, value in people.items():
#     new_dict[value]=key
# print(new_dict)
# # 14. **Find Keys with Value**: Given a dictionary and a value, create a list of all keys that have that value.
# people={'name':'Ali', 'age':23, 'work':'doctor'}
# value=23
# key_list=[]
# for i in people.keys():
#     if people[i]==value:
#         key_list.append(i)

# print(key_list)
# # 15. **Create a Dictionary from Lists**: Given two lists (one of keys and one of values), create a dictionary that pairs them.
# keys = ['name', 'age', 'work']
# values = ['Ali', 23, 'doctor']
# new_dict={}
# for i in range(len(keys)):
#     new_dict[keys[i]]=values[i]
# print(new_dict)
# # 16. **Check for Nested Dictionaries**: Given a dictionary, check if any values are also dictionaries.
# my_dict = {
#     'name': 'Ali',
#     'age': 23,
#     'address': {'city': 'Lahore', 'zip': 54000}
# }

# has_nested = any(isinstance(value, dict) for value in my_dict.values())
# print(has_nested)

# # 17. **Get Nested Value**: Given a nested dictionary, retrieve a value from within one of the inner dictionaries.
# my_dict = {
#     'name': 'Ali',
#     'age': 23,
#     'address': {'city': 'Lahore', 'zip': 54000}
# }
# print(my_dict['address']['city'])
# # 18. **Create Default Dictionary**: Create a dictionary that provides a default value for missing keys.
# my_dict = {
#     'name': 'Ali',
#     'age': 23,
#     'address': {'city': 'Lahore', 'zip': 54000}
# }
# my_dict.setdefault('book', 'not avaiable')
# print(my_dict)
# # 19. **Count Unique Values**: Given a dictionary, determine the number of unique values it contains.
# my_dict = {
#     'name': 'Ali',
#     'age': 23,
#     'city': 'Lahore'
# }

# unique_count = len(set(my_dict.values()))
# print(unique_count)

# # 20. **Sort Dictionary by Key**: Create a new dictionary sorted by keys.
# my_dict = {'b': 2, 'a': 1, 'c': 3}

# sorted_dict = dict(sorted(my_dict.items()))
# print(sorted_dict)

# # 21. **Sort Dictionary by Value**: Create a new dictionary sorted by values.
# m_dict = {'b': 2, 'a': 1, 'c': 3}
# sort_by_value=dict(
#     sorted(m_dict.items(), key= lambda i: i[1], reverse=True)
#     )
# print(sort_by_value)


# # 22. **Filter by Value**: Given a dictionary, create a new dictionary that only includes items with values that meet a certain condition.
# my_dict = {'a': 5, 'b': 15, 'c': 8, 'd': 20}

# # Using dictionary comprehension
# filtered_dict = {k: v for k, v in my_dict.items() if v > 10}

# print(filtered_dict)

# # 23. **Check for Common Keys**: Given two dictionaries, check if they have any keys in common.
# dict1 = {'a': 1, 'b': 2, 'c': 3}
# dict2 = {'b': 20, 'd': 4}

# # Convert keys to sets and check intersection
# common_keys = set(dict1.keys()) & set(dict2.keys())

# if common_keys:
#     print("Common keys:", common_keys)
# else:
#     print("No common keys")

# # 24. **Create Dictionary from Tuple**: Given a tuple of key-value pairs, create a dictionary from it.
# tuple_of_pairs = (('name', 'Ali'), ('age', 23), ('work', 'doctor'))

# # Convert tuple of pairs to dictionary
# tuple_of_pairs = (('name', 'Ali'), ('age', 23), ('work', 'doctor'))
# my_dict = dict(tuple_of_pairs)
# print(my_dict)

# # 25. **Get the First Key-Value Pair**: Retrieve the first key-value pair from a dictionary.
# my_dict = {'a': 5, 'b': 15, 'c': 8, 'd': 20}
# first_pair = list(my_dict.items())[0]
# print(first_pair)
#########################################