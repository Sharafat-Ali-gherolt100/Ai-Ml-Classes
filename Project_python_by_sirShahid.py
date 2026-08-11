print('-----------------------          My Money Manager            ----------------------- \n')
print('----------------------   The Project By Sir Shahid (Python)    ----------------------\n\n')
print('----------------------              Main Menu          ----------------------\n')

ExpacneList = []


def AddExPancefunction():
    AddExDate = input('Enter the Date of Expance ')
    AddExValue = int(input('Enter the Amount of Expance '))
    AddExCat = input('Enter the catergory of Expance ')
    AddExNote = input('Enter the Note of Expance ')

    Expance = {
        'date': AddExDate,
        'category': AddExCat,
        'amount': AddExValue,
        'note': AddExNote
    }

    ExpacneList.append(Expance)

    print('Expance Added Successfully !')


def ViewAllExpensesfunction():

    if len(ExpacneList) == 0:
        print('No Expances Found !')
    else:
        for Expance in ExpacneList:
            print(
                Expance['date'],
                Expance['category'],
                Expance['amount'],
                Expance['note']
            )


def SavetoFilefunction():

    File = open('expenses.csv', 'w')

    for Expance in ExpacneList:
        File.write(
            Expance['date'] + ',' +
            Expance['category'] + ',' +
            str(Expance['amount']) + ',' +
            Expance['note'] + '\n'
        )

    File.close()

    print('Expenses Saved Successfully !')


def LoadfromFilefunction():

    try:
        File = open('expenses.csv', 'r')

        for Line in File:
            Data = Line.strip().split(',')

            Expance = {
                'date': Data[0],
                'category': Data[1],
                'amount': int(Data[2]),
                'note': Data[3]
            }

            ExpacneList.append(Expance)

        File.close()

        print('Expenses Loaded Successfully !')

    except FileNotFoundError:
        print('No expenses file found !')


def Reportfunction():

    if len(ExpacneList) == 0:
        print('No Expances Found !')
    else:

        Total = 0

        for Expance in ExpacneList:
            Total = Total + Expance['amount']

        Average = Total / len(ExpacneList)

        Categories = {}

        for Expance in ExpacneList:

            Category = Expance['category']

            if Category in Categories:
                Categories[Category] = Categories[Category] + Expance['amount']
            else:
                Categories[Category] = Expance['amount']

        TopCategory = max(Categories, key=Categories.get)

        print('Total Spent :', Total)
        print('Average Per Entry :', Average)
        print('Category Spent Most :', TopCategory)


def Quitfunction():
    print('Thank u ')


while(True):

    print('___________________________  Main Menu  ___________________________')
    print(' 1. Add Expense')
    print(' 2. View All Expenses')
    print(' 3. Save to File')
    print(' 4. Load from File')
    print(' 5. Report')
    print(' 6. Quit')
    print('_______________________________________________________________')

    UserValue = int(input('Enter the Value to Do Operation '))

    if(UserValue == 1):
        AddExPancefunction()
        continue

    elif(UserValue == 2):
        ViewAllExpensesfunction()
        continue

    elif(UserValue == 3):
        SavetoFilefunction()
        continue

    elif(UserValue == 4):
        LoadfromFilefunction()
        continue

    elif(UserValue == 5):
        Reportfunction()
        continue

    elif(UserValue == 6):
        print('Thanks for Quit the Program Come Again Thank u !!!')
        break

    else:
        print('Select the Correct Option to Do something ! ')
        continue