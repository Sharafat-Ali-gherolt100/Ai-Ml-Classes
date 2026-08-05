# Python Functions: Practice Assignments
# Week 2 | Day 1 - Practical Task Sheet

# Task 1: The Coffee Shop Calculator (Easy)

def calculate_total(price, quantity):
    Total = price * quantity
    print('The ', quantity , 'coffees price is  :  ' ,  Total)
    return  Total


FinalTotal  = calculate_total(250, 3)
print(FinalTotal)



# 2nd Question 

def apply_discount(original_price, promo_code):
    promo_code = 'SAVE10'
    if(promo_code == 'SAVE10'):
        
        total_discount = original_price * 0.10
        new_price=original_price-total_discount
        print('after apply the Dicount The Price is :  ' , new_price)
        
    else:
        print('Without Discount the Price is : ' , original_price)
        return original_price
        
        
apply_discount(9000 , "SAVE1O")


ratings_list = [2,5,6,8,9,5,4]
def get_average_rating(ratings_list):
    sum = 0
    for i in ratings_list:
        # print(i)
        sum = sum + i
        print('The final sum is : ' , sum)
        ave = sum / len(ratings_list)
        print('The average is : ' , ave)
        

get_average_rating(ratings_list)



def usd_to_pkr(dollars):
    usd_amount = dollars * 278
    print('The Usd to Pkr Convert Money is : '  , usd_amount)
    return usd_amount


def is_within_budget(usd_amount, max_pkr_budget):
    usd_amount = usd_to_pkr(10)
    if(usd_amount < max_pkr_budget):
        print('Your money is enigh for Tour so : True' )
    else :
        print('Your money is NOT  enigh for Tour so : False', )

        

is_within_budget(10, 4000)



# Task 5: The Expedition Evaluator (Master Challenge)
daily_distances = [23,54,6,7,3,5,11];
def evaluate_trekker(trekker_name, daily_distances, has_medical):
    TotalDistance = 0
    has_medical = True
    for i in daily_distances:
        TotalDistance = TotalDistance + i
        print('The Total Distince is : ' , TotalDistance)
    aveDistance = TotalDistance / len(daily_distances)
    print('The average distance is : ' , aveDistance)
    if(TotalDistance >= 50 and aveDistance > 8 and has_medical):
        print(trekker_name , 'You are medical Fit U can Track' , has_medical)
    else:
        print(trekker_name , 'You are not Fir for BaseCamp Track', has_medical)
        


evaluate_trekker('ali' , daily_distances , True)