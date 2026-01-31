from collections import defaultdict
person=defaultdict(list)

person['name']='John'

person['skills'].append('sql')
person['skills'].append('sql')
person['skills'].append('py')
person['skills'].append('bi')
person['skills'].append('sql')
person['skills'].append('sql')
person['skills'].append('sql')

person['skills'].append('bi')
person['skills'].append('bi')
person['skills'].append('bi')
person['skills'].append('bi')

print(person)

nums = [10, 20, 30]
for num in nums:
    if num > 25:
        print("Large number found")
        break
else:
    print("No large numbers")


