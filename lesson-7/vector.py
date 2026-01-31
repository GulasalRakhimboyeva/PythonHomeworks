# class Myclass:
#     x=5
#     y=4
# print(Myclass)
# p1=Myclass()

# # print(p1.y)

# del p1
# print(p1.y)

class person:
    def __init__(self, name, age ):
        self.name=name
        self.age=age
    def greeting(self):
        print('Hello my name is '+ self.name)
p1=person('Ali', 23)

p1.greeting()