travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

#Function that will allow new countries to be added to the travel_log
def add_new_country(country_visited, visits_num, cities_visited):
    new_country = {
        "country": country_visited, 
        "visits": visits_num, 
        "cities": cities_visited
    }
    #another method
    #new_country = {}
    #new_country["country"] = country_visited
    #new_country["visits"] = visits_num
    #new_country["cities"] = cities_visited
  
    travel_log.append(new_country)
  
#Original exercise:
#add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
#print(travel_log)

#Extended practice:  
ask_country = input("What country have you visited?\n")
num_visits = input("How many times have you visited said country?\n")
visited_cities = input("Which cities have you visited in this country? Separate each city by a comma (e.g., Los Angeles, San Francisco)\n").split(', ')

add_new_country(ask_country, num_visits, visited_cities)
print(travel_log)

