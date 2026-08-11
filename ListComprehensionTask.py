# GB Guide Tourist Manifest & Analytics
# You are handed a nested data structure: a list of dictionaries representing tourists. Your task
# involves two steps to shape the data for reporting:
# Use a list comprehension to extract a list of names of all tourists whose destination is "Fairy
# Meadows".
# Calculate the average age of all tourists in the entire list (using list comprehensions and Week 2
# math foundations).


tourists = [
 {"name": "Sara", "age": 28, "destination": "Skardu"},
 {"name": "John", "age": 34, "destination": "Fairy Meadows"},
 {"name": "Bilal", "age": 22, "destination": "Khaplu"},
 {"name": "Emma", "age": 29, "destination": "Fairy Meadows"},
 {"name": "Tariq", "age": 45, "destination": "Skardu"}
 ]

# 2. Calculate 'average_age'

f =[];
Tage = 0
for i in tourists:
    if i["destination"]== "Fairy Meadows":
        f.append(i)
        
        
print(f)

dic2 = [i['name'] for i in tourists if i["destination"] == 'Fairy Meadows']
dic3 = sum([i['age'] for i in tourists]) / len(tourists) 
# ang=sum(dic3)/len(tourists)
print(dic3)
# print(ang)

