# Question 1 
# Write a function called city_country() that takes in the name of a city and its country. 
# The function should return a string formatted like this: "Santiago, Chile" Call your function with at least three city-country pairs, and print the values that are returned.

# Solution---1
def city_country(city, country):

    city_country = f"{city} {country}"
    print(city_country)
    return city_country

city_country("Santiago", "Chile")
city_country("Mdarid", "Spain") # Hala country
city_country("Barcelona", "Spain") # Visca barca

