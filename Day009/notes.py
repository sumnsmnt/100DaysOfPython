######## Dictionary #########

# programming_dictionary = {
#     "Bug": "An error in a program that prevents the program from running as expected.", 
#     "Function": "A piece of code that you can easily call over and over again.",
#     }

# print(programming_dictionary)

# # Retrieving items from dictionary.
# print(programming_dictionary["Bug"])

# # Adding new items to dictionary.
# programming_dictionary["Loop"] = "The action of doing something over and over again."
# print(programming_dictionary)

# # Clear an existing dictionary.
# programming_dictionary = {}
# print(programming_dictionary)

# # Edit an item in a dictionary
# programming_dictionary["Bug"] = "Bug is an insect"
# print(programming_dictionary)

# # Loop through a dictionary
# for key in programming_dictionary:
#     print(key)
#     print(programming_dictionary[key])


# # 1. You have access to a database of student_scores in the format of a dictionary. The keys
# # in student_scores are the names of the students and the values are their exam scores.
# # Write a program that converts their scores to grades. by the end of your program, you should
# # have a new dictionary called student_grades that should contain student names for keys and
# # thier grades for values. The final version of the student_grades dictionary will be checked.
# # Scoring criteria:
# # Score 91 - 100: Grade = "Outstanding"
# # Score 81 - 90: Grade = "Exceeds Expectations"
# # Score 71 - 80: Grade = "Acceptable"
# # Score 70 or laser : Grade = "Fail"

# student_scores = {
#     "Suman": 69,
#     "Sujan": 79,
#     "Sajan": 89,
#     "Sagar": 99,
# }
# # Todo 1: Create an empty dictionary called student_grades
# student_grades = {}

# # Todo 2: Write your code below to add the grades to student_grades
# for student in student_scores:
#     score = student_scores[student]
#     if score > 90:
#         student_grades[student] = "Outstanding"
#     elif score > 80:
#         student_grades[student] = "Exceeds Expection"
#     elif score > 70:
#         student_grades[student] = "Acceptable"
#     else:
#         student_grades[student] = "Fail"

# print(student_grades)


######### Nested Dictionary #########

# # Dictionary key: value pair
# capitals = {
#     "India": "New Delhi",
#     "France": "Paris",
#     "Germany": "Berlin",
# }

# # Nesting List in a Dictionary
# travel_log = {
#     "India": ["Delhi", "Mumbai", "Kolkata", "Bangalore"],
#     "France": ["Paris", "Lille", "Dijon"],
#     "Germany": ["Berlin", "humburg", "Stuttgart"],
# }

# # Nesting Dictionary in a Dictionary
# travel_vlog = {
#     "India": {"cities_visited": ["Delhi", "Mumbai", "Kolkata", "Bangalore"], "total_visit": 12},
#     "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visit": 2},
# }

# # Nesting Dictionary in a list
# travel_v_log = {
#     {
#         "country": "India", 
#         "cities_visited": ["Delhi", "Mumbai", "Kolkata", "Bangalore"], 
#         "total_visit": 12,
#         },
#     {
#         "country": "France",
#         "cities_visited": ["Paris", "Lille", "Dijon"], 
#         "total_visit": 2,
#         },
# }


# 2. Write a program that adds to a travel_log. The travel_log which is a List that
# contains 2 Dictionaries.

travel_log = [
    {
        "country": "India", 
        "visits": 12,
        "cities": ["Delhi", "Mumbai", "Kolkata", "Bangalore"], 
        },
    {
        "country": "France",
        "visits": 2,
        "cities": ["Paris", "Lille", "Dijon"], 
        },
]

def add_new_country(country_visited, total_visited, city_visited):
    new_country = {}
    new_country["country"] = country_visited
    new_country["visits"] = total_visited
    new_country["cities"] = city_visited
    travel_log.append(new_country)

add_new_country("United Kingdom", 2, ["London", "xyz", "abc"])
print(travel_log)