##### FOR LOOP #####

fruits = ["apple", "mango", "banana"]
for fruit in fruits:
    print(fruit)
    print(fruit + " shake")


# 1. Write a program that calculates the average student height from a list of heights.
# Without using sum() or len() functions
student_heights = [180, 192, 176, 155, 179, 181, 149]

height_sum = 0
total_students = 0
for height in student_heights:
    height_sum += height
    total_students += 1
print(height_sum / total_students)

# 2. Write a program that calculates the highest score from a list of scores.
# without using max() or min() function.
all_scores = [78, 89, 91, 96, 98, 99, 33, 98]
highst_score = 0
for score in all_scores:
    if score > highst_score:
          highst_score = score
    else:
         continue
print(f"The highest score is: {highst_score}")


### range() function in for loop ###

# this will print from 1 to 10. whatever laste number is mentioned in the range, it will
# always go 1 step less than that. let the range is from 1 to n, then it will print 1 to n-1
for number in range(1, 11):
    print(number)
# the range will go from 2 to 10, incremented by 2 at a time. 2 is step counter in the function
for number in range(1, 11, 2):
    print(number)

# 3. Write a program that calculates the sum of all the even numbers from 1 to 100, including 1 and 100

sum = 0
for number in range(1, 101):
    if number % 2 == 0:
        sum += number
    else:
        continue
print(sum)


# 4. Write a program that automatically prints the solution to the FizzBuzz game.
# Your program should print each number from 1 to 100 in turn.
# When the number is divisible by 3 then instead of printing the number it should print "Fizz"
# When the number is divisible by 5 then instead of printing the number it should print "Buzz"
# When the number is divisible by both 3 and 5 then instead of printing the number it should print "FizzBuzz"

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("buzz")
    else:
        print(number)