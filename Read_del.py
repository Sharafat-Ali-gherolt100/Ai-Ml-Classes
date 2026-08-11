# with open('myfile.txt' , 'r') as f:
#     content = f.read()
#     for line in content:
#         print(line)

# with open('Data.csv' , 'r') as f:
#     content = f.read()
#     for line in content:
#         print(line)
        
        
# with open('Data.csv' , 'r') as f:
#     content = f.read()
#     for x in content:
#         print(x)
        
        
# Mystring = '\n\n    Hello this is the New String        ';
# print(Mystring.strip())
 
 
# li = Mystring.split()
# print(li)

# name,mark,city = li
# print(name,mark,city)


MyList = []
with open('Data.csv' , 'r') as f:
    rows = f.read()
    row_1 = rows.split('\n')
    for row in row_1[1:]:
        li = row.split(",")
        print(li)
        name,mark,city = li
        dic = {"name" : name , "mark" : mark, "city" : city}
        MyList.append(dic)
                
print(MyList)




