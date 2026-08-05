# Student_Dictinary = {
#     "science" : 39 , "math" : 44 , "computer" : 87
# }
# TotalMarks = 0
# for key , value in Student_Dictinary.items():
#     # print(key,value)
#     TotalMarks = TotalMarks + value
# print('The Total Marks in Subject is : '  , TotalMarks)


# Another_Dictionary = {
    
#     "name" : "sharafat",
#     "Fname" : "Ayoub",
#     "Isstudent" : True,
    
# }
# for k,v in Another_Dictionary.items():
#     print(k,v)
    
    

# Another Task by sir Shahid In Dictionary 

# Student_Dictinary2 = {
#     "science" : 39 , "math" : 44 , "computer" : 87
# }
# sum = 0
# ave  = 0

# for k,v in Student_Dictinary2.items():
#     sum = sum + v
#     ave = sum / len(Student_Dictinary2)
#     print(k,v)
# print('The sum of marks is : ' , sum)  
# print('The ave of marks is : ' , ave)  



# student_record = {
    
#     "name" : "Ali",
#     "Age" : 24,
#     "course" : "Pyhton",
#     "python_score" : 50
    
# }

# for key , value in student_record.items():
#     print(key,value)
    
    
# # Developer Profile 

# dev_profile = {"name": "Ali", "role": "JuniorDev", "language": "Python"} 
# dev_profile.update({"role" : "SeniorDev"})
# dev_profile.update({"knows_fastapi" : True})
# # dev_profile{"role" : "SeniorDev"}

# for key ,value in dev_profile.items():
#     print(key,value)



# # 3rd Question
# phone_prices= {
#     "iPhone 12" : 343534,
#     "Samsung S22" : 235352,
#     "Techno" : 23525,
#     "oppo" : 634564,
# }

# for k,v in phone_prices.items():
#     # print(k,v)
#     if(v < 100000):
#         print('For U Avaible Phone')
#         print(k,v)
        
        

# tourists = [
#     {
#         "name": "Rafay",
#         "country": "Nepal",
#         "has_paid": False
#     },
#     {
#         "name": "Younus",
#         "country": "Iran",
#         "has_paid": True
#     },
#     {
#         "name": "Azeem",
#         "country": "Iraq",
#         "has_paid": False
#     }
# ]

# for tourist in tourists:
#     if tourist["has_paid"] == False:
#         print(f"Payment pending for {tourist['name']} from {tourist['country']}.")
        
        
        
        

# 5th Question 

# The Ecommerce Api Parser
# scenrio : 
    # your next.js frontend has just Recevied a complex data package  from your backend database . you need to extrct infromation , calculate  totals and check user  privileges 
    
    
api_data = { "user" : ("Ahmed " , "Premium"), "cart" : [{"item" : "keyboard", "price": 5000},{ "item" : "Moniter", "price" : 35000}]}
    
for k in api_data["user"]:
        print(k)
        
for k,v in api_data["cart"]:
    # for v in 
    print(k,v)
    