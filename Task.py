EvenList  = []
OddList  = []

Num = int(input('Enter the Number'))
for i in range(1 ,20):
    Res = Num*i
    print(Num," X ",i," = ",Res)
    
    if(Res % 2 == 0 ):
        EvenList.append(Res)
    else:
        OddList.append(Res)
print(OddList)
print(EvenList)