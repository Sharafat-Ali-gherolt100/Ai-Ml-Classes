scores = [10, 20, 30, 40, 50, 60, 70, 80, 90];
TotalScore = 0
Total_Fifties = 0


for item in scores:
    TotalScore = TotalScore + item
    
    if(item > 50):
        print(item)
print('The TotalScore in Runs :  ' , TotalScore)

print()