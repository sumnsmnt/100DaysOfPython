########## DEBUGGING ###########

# # 1. Describe Problem
# def my_function():
#     # this loop will go until 19, so i == 20 will never execute.
#     # for i in range(1, 20):
#     # To debug the problem I increased the range from 20 to 21.
#     for i in range(1, 21):
#         if i == 20:
#             print("You got it")
# my_function()


# # 2. Reproduce the bug
# from random import randint
# dice_nums = ["One", "Two", "Three", "Four", "Five", "Six"]
# # This line throwing error sometimes
# # dice = randint(1, 6)
# # To find the issue we have go through each element and we found
# # that for the value 6 we are getting error, so the range will be
# # (0, 5) as indexing starts from 0
# dice = randint(1, 5)
# print(dice_nums[dice])


# # 3. Play Computer
# year = int(input("What's your year of birth? "))
# if year > 1990 and year <= 1999:
#     print("Your are millenial.")
# elif year > 1999:
#     print("You are Gen Z")


# # 4. Fix the Errors
# # This age variable stores input as a string and we can't compare 
# # a string with an integer, for that we need to convert it into int.
# # age = input("How old are you? ")
# age = int(input("How old are you? "))
# if age > 18:
#     print(f"You are an adult as you are {age} years old.")


# # 5. Print is your friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# # Now I can look fro word_per_page variable as the probles lies here
# # So I can see that insted of "=" I used "=="
# # word_per_page == int(input("Number of words per page: "))
# word_per_page = int(input("Number of words per page: "))
# total_words = pages * word_per_page
# # to find the problem, first print out all the variables, so that 
# # we can find out easily where the problem started.
# print(f"pages = {pages}")
# print(f"words_per_page = {word_per_page}")
# print(total_words)


# # Use a Debugger
# def mutate(a_list):
#     b_list = []
#     for item in a_list:
#         new_item = item * 2
#         b_list.append(new_item)
#     print(b_list)

# mutate([1, 2, 3, 4, 5, 6, 7])