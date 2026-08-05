# while True:
#     print('Hello')

# while True:
#     userInput = int(input('Enter the Number'))
#     print(userInput)
#     if(userInput==5):
#         break

# regular keyword

secret = 39
range = 5  
while range:
    userInput = int(input('Enter the number'))
    range = range -1
    print(userInput)
    if(userInput > 39):
        print('Enter the number below 39')
        print('Remaining CHANCE ' , range )
    elif(userInput < 39):
        print('Enter the number greater ', range)
        print(f'Remaining CHANCE {range}'  )
    elif(userInput==39):
        print('Now Correct ')
        
    elif(userInput<1):
        print("You losse")
        print('Remaining CHANCE ' , range )
        
       