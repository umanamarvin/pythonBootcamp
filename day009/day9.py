# 1 Dictionaries

programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and over again"}

print (programming_dictionary["Bug"])


# 2 creating a dictionary grades from an other dictionaty called scores

students_scores = {
    "Harry": 81,
    "Ron" : 78,
    "Hermione": 99,
    "Neville": 62,
}

students_grades = {}
score = 0

for student in students_scores:
    score = students_scores[student]

    if score >= 91 and score <= 100:
        students_grades[student] = "Outstanding"
    elif score >= 81 and score <= 90:
        students_grades[student] =  "Exceeds expectations"
    elif score >= 71 and score <= 80:
        students_grades[student] =  "Acceptable"
    elif score <= 70:
        students_grades[student] =  "Fail"
    
for student in students_grades:
    print (student + " --> " + students_grades[student])


# 3 Nesting lists in dictionaries

travel_log = {
    "France": ["Paris", "Lille", "Dijon", {"Cities_visited": ["Paris", "Lille"]}],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"]
}
print (travel_log)

#4 Nesting dictionaries in lists

travel_log = [
    {
    "country": "France",
    "cities_visited": ["Paris", "Lille", "Dijon1"],
    "total_visits": 12
    },
    {
    "country": "Germany",
    "cities_visited": ["Berlin", "Hamburg", "Heidelberg"],
    "total_visits": 5
    }
]

def add_new_country (pais,ciudad,visitas):
    new_country = {}
    new_country["country"] = pais
    new_country["cities_visited:"] = ciudad
    new_country["visits"] = visitas
    travel_log.append(new_country)

    print (travel_log)



country = input ("What country do you want to add? ")

cities = input ("Type the cities separated with a espace: ")
cities = cities.split()


visits = int(input("How many times did you visit? "))

add_new_country (country, cities, visits)
