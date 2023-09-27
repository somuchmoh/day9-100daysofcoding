#How to create a python dictionary
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again.",
}
print(programming_dictionary["Bug"])

#Adding a new entry to the python dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again."
print(programming_dictionary)

#create an empty dictionary
empty_dictionary = {}

#Wipe an existing dictionary 
# programming_dictionary = empty_dictionary

#Edit an item in a dictionary 
programming_dictionary["Bug"] = "A moth in your computer"
print(programming_dictionary)

#Loop through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])


#Nesting Dictionaries
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

#Nesting a list in dictionary
travel_log = {
    "France":["Paris", "Lille", "Dijon"],
    "India": ["Delhi", "Mumbai", "Bangalore"],
}

#Nesting a dictionary in a dictionary
travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "India": {"cities_visited": ["Delhi", "Mumbai", "Bangalore"], "total_visits": 9}
}
print(travel_log)


#Nesting a dictionary in a list 
travel_log = [   #List start
{     #dictionary 1 start
    "country": "France", 
    "cities_visited": ["Paris", "Lille", "Dijon"],               "total_visits": 12,
},
{     #dictionary 2 start
    "country": "India", 
    "cities_visited": ["Delhi", "Mumbai", "Bangalore"],          "total_visits": 9
}
]
