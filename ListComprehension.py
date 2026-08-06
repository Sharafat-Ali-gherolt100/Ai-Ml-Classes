# distance_in_meters = [1000, 2000, 3423, 1289, 1989]
# Convert_Distance_list = [i / 1000   for i in distance_in_meters ]
# print(Convert_Distance_list)



# map method , def conversion 

NewList = [324,5352,3424,656,9]
def Newfunction(i):
    if(i % 2 == 0):
        return 'even'
    else :
        return 'odd'
            
UpdatedList =  list(map(Newfunction , NewList))
print(UpdatedList)

# names = ['shahid' , 'khan', 'ali' , 'rafay']
# age = [22,44,12,76]
# FinalDic = {}
# for i,k in zip(names, age):
#     print(i,k)
#     # FinalDic.update({i:k})
#     FinalDic[i]=k
    
# print(FinalDic)

# Andic = {x:y for x,y in zip(names,age)}
# print(Andic)