rouz=int(input("rouze miladi ro vared konid."))
mah=int(input("mahe miladi ro vared konid."))
sal=int(input("sale miladi ro vared konid."))
if sal%4 !=0 :
    print("kabise nist.")
    kabise=False
elif sal%4 ==0 and sal%400 ==0 :
    print("kabise ast.")
    kabise=True
elif sal%4 ==0 and sal%100 ==0 :
    print("kabise nist.")
    kabise=False    
elif sal%4 ==0 :
    print("kabise ast.")
    kabise=True

if kabise==True:
    list1=[31,29,31,30,31,30,31,31,30,31,30,31]
if kabise==False:
    list1=[31,28,31,30,31,30,31,31,30,31,30,31]

total=sum(list1[:mah-1])+rouz
total1=str(total)
print("Rouze "+total1+"ome sal madde nazar ast.")
