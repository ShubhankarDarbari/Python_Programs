import random
world_capitals = {"India": 'Delhi',
		              "Pakistan": 'Islamabad',
                  "United States of America": 'Washington D.C',
                  "China": 'Beijing',
                  "Malaysia": 'Kuala Lumpur',
                  "Thailand": 'Bangkok',
                  "France": 'Paris',
                  "Italy": 'Rome',
                  "Spain": 'Madrid',
                  "Australia": 'Sydney',
		              "Srilanka": 'Colombo',
                  "Afganistan": 'Kabul',
                  "South Africa": 'Cape Town',
                  "Bangladesh": 'Dhaka',
                  "Russia": 'Moscow'
                  }
counter = 0
countries = list(world_capitals.keys())

while True:
    country = random.choice(countries)
    capital = world_capitals[country]
    Entered_Value = input("What is the capital of " + country + " ?")

    if Entered_Value == capital:
        counter += 1
        print(counter)
        
    elif Entered_Value == "End":
        break
        
     
    else:
        print("Please try again.")
        counter -= 1
        print(counter)
