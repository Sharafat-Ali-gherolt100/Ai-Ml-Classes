guesthouse = {"name" : "k2 view guesthouse", "rooms" : 6, "price" : 1500}
location = {35.3, 75.6}
guests = [10, 9, 10, 40, 8, 10, 11]
base_fee = 2000

def bill(room):
    night = 1500
    TotalBill = room * night
    print('The Total bill of 03 Room Per Night is : ' ,TotalBill)

bill(3)


# 2nd Question 

Name = guesthouse["name"]
price = guesthouse["price"]

print(Name.upper())
print(price)



# 3rd Question 
max_val = 0
bussiest_mon = 0
for x in range(5,8):
    Guest_value = 5 * x
    print("Month", x, "Guests:", Guest_value)

    if(x > max_val):
        max_val = x
        bussiest_mon = x

print("Busiest Month:", bussiest_mon)    


# 4th Question 

def Total(months):
     base_fee = 2000
     monthfee = 1500
     monthlfee =  months * monthfee
     finalPrice = base_fee + monthlfee
     print('Full BIll :  '  , months , 'nights ' , finalPrice)


Total(4)



# 5th Question 
total = 0
mean = 0
for x in guests:
    total = total + x
    mean = total / len(guests)
    Sorted_list = sorted(guests)
    
print(Sorted_list)
print('Mean : ' , mean)
print('Median  : ', 10 )
print('Mode  : ', 10 )

# bonus 

Total_guest = 0
nights = 0

for x in guests:
    Total_guest = Total_guest + x
    nights = nights + 1
    
    if(Total_guest > 50):
        break
    
print('The Guest Reached 50  ' , 'after ' , nights, 'nights')