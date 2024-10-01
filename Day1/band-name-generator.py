# Ask the user their name
name = (input("Hi! Please enter your name :) \n"))

# Greet the user
print("Welcome to Band Name Generator,", name)

# Ask the user of their city name
city = (input("What's the name of your city? \n"))

# Ask the user of their favourite movie name
movie = (input("What's your favourite movie? \n"))

# Combine city and movie name to generate a unique band name
print("Hi", name + ", your band name is " + movie + " " + city)