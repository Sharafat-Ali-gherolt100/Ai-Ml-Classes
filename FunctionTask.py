def WeatherFunction(value):
    if(value=='sunny'):
        print('Go Trekking in Shigar Valley')
    elif(value == 'rainy'):
        print('Vist the Shigar Fort Museum ')
        
    else:
        print('Visit the Local Visters')
        
    

Weatherlist = ['sunny', 'rainy', 'snowy']

for val in Weatherlist:
    WeatherFunction(val)