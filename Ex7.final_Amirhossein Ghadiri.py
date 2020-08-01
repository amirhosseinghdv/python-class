def fib(arg):
    if arg< 0:
        print("vorodi ghalat")
    elif arg==1:
        return 0
    elif arg==2:
        return 1
    else:
        return fib(arg-1)+fib(arg-2)



def fib_list(arg):
    try:
        if arg < 1:
            print("adade mosbat nadadid.")
        else:
            list1=[]
            for i in range(1,int(arg)+1):
                list1.append(fib(i))
            print(list1)
    except:
        print("vorodi adad nist.")          
          
        
