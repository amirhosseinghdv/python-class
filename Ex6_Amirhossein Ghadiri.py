"""#45:
total=0
while total <= 50:
    num=float(input("Please input a number: "))
    total += num
    plus=str(total)
    print("The total is: "+ plus)
"""

    
"""#46:
num=float(input("Please enter a number: "))
while num <= 5:
    num=float(input("Please enter a number: "))
    numstr=str(num)
print("The last number you entered was a "+numstr)
"""


"""#47:
num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
total=num1+num2
Q=input("Do you want to add another number?")
while Q=="y":
    num3=int(input("Enter another number: "))
    total+=num3
    Q=input("Do you want to add another number?")
totalstr=str(total)    
print("total = "+totalstr)
"""


"""#48:
name1=input("Who do you want to invite to the party? ")
print(name1+" has now been invited.")
count=1
Q=input("Do you want to invite somebody else? ")
while Q.lower()=="yes":
    name2=input("Type his name: ")
    print(name2+" has now been invited.")
    count+=1
    Q=input("Do you want to invite somebody else? ")
count1=str(count)    
print("You are inviting "+count1+" people to the party.")
"""


"""#49:
compnum=50
count=0
num1=int(input("Enter a number: "))
while num1!=compnum:
    if num1<compnum:
        print("Too low")
        count+=1
        num1=int(input("another guess? "))
    elif num1>compnum:
        print("Too high")
        count+=1
        num1=int(input("another guess? "))
if num1==compnum:
    count+=1
    count1=str(count)        
    print("Well done, you took "+count1+" attempts.")
"""


"""#50:
num1=int(input("Enter a number between 10 and 20: "))
while num1<10 or num1>20:
    if num1<10:
        print("Too low")
        num1=int(input("Try again for a number between 10 and 20: "))
    if num1>20:
        print("Too high")
        num1=int(input("Try again for a number between 10 and 20: "))
if 10<=num1<=20:
    print("Thank you")
"""


#51:
#I dont understand the question.


    




    
    
