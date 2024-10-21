
"""

1. Prompt user by asking what they want?
-> Check the user's input to decide what to do next.
-> The prompt should show everytime action has completed, e.g. once the drink is dispensed.
The prompted should show again to seve the next customer.

2. Turn off the machine by entering "off"
-> For maintainers of the coffee machine, they can use "off" as the secret word to turn off
the machine. Your code should end excution when this happens.

3. Print report
-> When the user enters "report to the prompt, a report should be generated that shows
the current resouces values.

4. Check resources are sufficient?
-> When the user chooses a drink, the program should check if there are enough resources
to make that drink.
-> e.g. if "latte" requires 200ml water but there is only 100ml left in the machine. It
should not continue to make the drink but prints "Sorry there is not enough water."
-> The same should happen if another resources is not sufficient.

5. Process currencies
-> If there are sufficient resouces to make the drink selected, then the program should 
prompt the user to insert notes.
-> Calculate the monetary value of the notes inserted.

6. Check transaction successful?
-> Check that the user has inserted enough money to purchase the drink they selected.
e.g. "latte" costs Rs.150, but they only inserted Rs.100 then after calculating the 
program should say "Sorry that's not enough money. Money refunded."
-> But if the user has inserted enough money, then the cost of drink gets added to the 
machine as a revenue and this will be reflected the next "report" is triggered.

7. Make Coffee
-> If the transaction is successful and there are enough resources to make the drink which 
the user selected, then the ingredients to make the drink should be deducted from the
coffee machine resources.
-> e.g. report before purchasing "latte"
Water: 300ml
Milk: 200ml
Coffee: 100gm
Money: 0rs
-> report after purchasing "latte"
Water: 100ml
Milk: 50ml
Coffee: 76gm
Money: 150rs

"""