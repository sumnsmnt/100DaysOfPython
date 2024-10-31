# You are going to create a program which will mark a spot wit an ✅.
# the map is made of 3 rows of blank starts.
# ["⭐", "⭐", "⭐"]
# ["⭐", "⭐", "⭐"]
# ["⭐", "⭐", "⭐"]
# Your program should allow you to enter the position of the treasure using a two-digit system.
# The first digit is the horizontal column number and the second digit is the vertical row number.

row1 = ["⭐", "⭐", "⭐"]
row2 = ["⭐", "⭐", "⭐"]
row3 = ["⭐", "⭐", "⭐"]

map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

position = input("Where you want to put the treasure? ")

column = int(position[0])
row = int(position[1])
# as indexing starts from 0, 3 will be out of lists, that's why -1 from row and column
map[row-1][column-1] = "✅"

# We can do step be step like below lines as well
# final_position = map[column-1]
# final_position[row-1] = "✅"

print(f"{row1}\n{row2}\n{row3}")