# ### Task 4
# Write a program that contains the following lists of lists:
# python
# universities = [
#     ['California Institute of Technology', 2175, 37704],
#     ['Harvard', 19627, 39849],
#     ['Massachusetts Institute of Technology', 10566, 40732],
#     ['Princeton', 7802, 37000],
#     ['Rice', 5879, 35551],
#     ['Stanford', 19535, 40569],
#     ['Yale', 11701, 40500]
# ]


# Define a function, _enrollment_stats()_, that takes, as an input, 
# a list of lists where each individual list contains three elements: 
# (a) the name of a university, (b) the total number of enrolled students, 
# and (c) the annual tuition fees.

# _enrollment_stats()_ should return two lists:
#  the first containing all of the student enrollment values 
# and the second containing all of the tuition fees.

# Next, define a _mean()_ and a _median()_ function.
#  Both functions should take a single list as an argument and 
# return the mean and median of the values in each list.

# Using universities, _enrollment_stats()_, _mean()_, and _median()_,
#  calculate the total number of students, the total tuition, 
# the mean and median of the number of students,
#  and the mean and median tuition values.

# Finally, output all values, and format the output so that it looks like this:


# ******************************
# Total students: 77,285
# Total tuition: $ 271,905

# Student mean: 11,040.71
# Student median: 10,566

# Tuition mean: $ 38,843.57
# Tuition median: $ 39,849
# ******************************

# solution
universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]

def enrollment_stats(data):
    students_list=[]
    tuitions_list=[]
    for item in data:
        students_list.append(item[1])
        tuitions_list.append(item[2])
    return students_list, tuitions_list

students, tuitions=enrollment_stats(universities)


def mean(values):
    return sum(values)/len(values)


def median(values):
    sorted_values = sorted(values)
    n = len(sorted_values)
    mid = n // 2
    if n % 2 == 1:
        return sorted_values[mid]
    else:
        return (sorted_values[mid - 1] + sorted_values[mid]) / 2


print("********************************")
print(f'Total students: {sum(students):,.2f}')
print('Total tuition:', f'${sum(tuitions):,.2f}')
print()
print('Student mean:', f'{mean(students):,.2f}')
print('Student median:', f'{median(students):,.2f}')
print()
print(f'Tuition mean: ${mean(tuitions):,.2f}')
print(f'Tuition median: ${median(tuitions):,.2f}')
print("********************************")
