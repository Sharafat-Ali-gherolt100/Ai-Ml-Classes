diction2 = [{'name' : 'Khan' , 'age' : '33' , 'city' : 'skardu'},
            {'name' : 'rafay' , 'age' : '43' , 'city' : 'gilgit'},
            {'name' : 'younus' , 'age' : '23' , 'city' : 'Chitral'}]

with open('NewData.csv' , 'w') as f:
    for x in diction2:
        f.write(x["name"] + " , " + x['age'] + ' , ' + x['city'] + '\n')
    