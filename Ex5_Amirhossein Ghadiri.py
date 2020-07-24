"""#69:
tuple1 = ("iran", "america", "canada", "italy", "spain")
print(tuple1)
country = input("please enter one of the shown countries: ")
index1 = tuple1.index(country)
print(index1 + 1)
"""


"""#70:
tuple1 = ("iran", "america", "canada", "italy", "spain")
print(tuple1)
country_num = int(input("please enter the number of country you choose: "))
print(tuple1[country_num - 1])
"""


"""#71:
sports=["football", "table tennis"]
user_sport = input("whats your favourite sport? ")
sports.append(user_sport)
sports.sort()
print(sports)
"""


"""#72:
list1 = ["math", "geometry", "algebria", "biology", "chemistry", "physics"]
print(list1)
answer = input("which of these subjects you don't like? ")
list1.remove(answer)
print(list1)
"""


"""#73:
food1 = input("Enter your first favorite food: ")
food2 = input("Enter your second favorite food: ")
food3 = input("Enter your third favorite food: ")
food4 = input("Enter your fourth favorite food: ")
dict_foods = {1: food1, 2: food2, 3: food3, 4: food4}
print(dict_foods)
delteted_food = int(input("which food number you want to get rid of: "))
dict_foods.pop(delteted_food)
dict_foods.sort()
print(dict_foods)
#نتونستم با گرفن ارزش حذف کنم. 
#ديکشنري که سورت نداره.
"""


"""#74:
#74:
colors=["red", "blue", "brown", "white", "black", "green", "yellow", "grey", "orange", "purple"]
adad1=int(input("enter a number from 0 to 4: "))
adad2=int(input("enter a number from 5 to 9: "))
print(colors[adad1:adad2])
"""


"""#75:
list1=[591, 888, 729, 975]
print(list1[0])
print(list1[1])
print(list1[2])
print(list1[3])
num=int(input("Enter a three digit number: "))
if num in list1:
    print(list1.index(num)+1)
else:
    print("That is not in the list.")
"""


"""#76:
person1=input("Please enter the names of three people you want to invite to the party: ")
person2=input()
person3=input()
list1=[person1, person2, person3]
Q=input("Do you want to invite another person? ")
n=3
while Q == "yes" :
    n+=1
    next_person=input("Enter the next persons name: ")
    list1.append(next_person)
    Q=input("Do you want to invite another person? ")
print(n)
"""


"""#77:
person1=input("Please enter the names of three people you want to invite to the party: ")
person2=input()
person3=input()
list1=[person1, person2, person3]
Q=input("Do you want to invite another person? ")
n=3
while Q == "yes" :
    n+=1
    next_person=input("Enter the next persons name: ")
    list1.append(next_person)
    Q=input("Do you want to invite another person? ")
print(list1)
choice=input("Please choose and type one of the names in the list: ")
position = str(list1.index(choice)+1)
print("position of the "+choice+" in list is "+position+". ")
q2=input("Do you still want "+choice+" to come to the party? ")
if q2=="no":
    list1.remove(choice)
print(list1)
"""


"""#78:
list1=["series", "football", "movie", "music"]
print(list1[0])
print(list1[1])
print(list1[2])
print(list1[3])
new=input("Please enter a new show name: ") 
position=int(input("the position in which you want to put it in(0to4): "))
list1.insert(position,new)
print(list1)
"""


"""#79:
nums=[]
n=0
for i in range (0,3):
    number=input("Please enter 3 numbers: ")
    nums.append(number)
    n+=1
    if n==2:
        nums1=nums.copy()
    if n==3:
        Q=input("Do you still want the last number saved? ")
        if Q=="no":
            print(nums1)
        else:
            print(nums)
"""
