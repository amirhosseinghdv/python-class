sal=int(input("sale miladi ro vared konid."))
if sal%4 !=0 :
    print("kabise nist.")
elif sal%4 ==0 and sal%400 ==0 :
    print("kabise ast.")
elif sal%4 ==0 and sal%100 ==0 :
    print("kabise nist.")
elif sal%4 ==0 :
    print("kabise ast.")

