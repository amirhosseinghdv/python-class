def date(rouz,mah,sal):
    if sal%4 !=0 :
        kabise=False
    elif sal%4 ==0 and sal%400 ==0 :
        kabise=True
    elif sal%4 ==0 and sal%100 ==0 :
        kabise=False    
    elif sal%4 ==0 :
        kabise=True
    if kabise==True:
        list1=[31,29,31,30,31,30,31,31,30,31,30,31]
    if kabise==False:
        list1=[31,28,31,30,31,30,31,31,30,31,30,31]
    total=sum(list1[:mah-1])+rouz
    total1=str(total)
    return total
