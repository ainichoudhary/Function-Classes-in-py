# modules
from utils import find_max

numbers = [20,3,4,6]
# max = find_max(numbers)
# print(max)

# or
print(max(numbers))


# classes
# inheritance
class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal):
    pass


class Cat(Mammal):
    pass


dog1 = Dog()
dog1.walk()

# simple class and constractor
class Person:
    def __init__(self,name):
        self.name = name
    def talk (self):
        print(f"Hi i am {self.name} ")

obj= Person("qurat")
obj.talk()

obj2 = Person("aini")
obj2.talk()



class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def move(self):
         print("move")

    def draw(self):
        print("draw")

point1 = Point(10,20)
Point.x = 11
print(Point.x)
# point1.x = 10
# point1.y = 20
# print(point1.x)
# point1.draw()



def emoji_converter(message):
    word = message.split(" ")
    emoji = {
        ":)": "😆",
        ":(": " 😔"
    }
    output = " "
    for i in word:
        output += emoji.get(i, " !") + " "

    return output

message = input(" > ")
print(emoji_converter(message))


def square(number):
    return number * number


result = square(7)
print(result)
