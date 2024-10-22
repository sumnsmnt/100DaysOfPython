class MoneyMachine:

    CURRENCY = "₹"

    Note_Values = {
        "10₹ notes": 10,
        "20₹ notes": 20,
        "50₹ notes": 50,
        "100₹ notes": 100,
    }

    def __init__(self):
        self.profit = 0
        self.money_received = 0

    def report(self):
        """Prints the current profit"""
        print(f"Money: {self.CURRENCY}{self.profit}")

    def process_coins(self):
        """Calculate the the total money paid by the user."""
        print("Please provide the money.")
        for note in self.Note_Values:
            self.money_received += int(input(f"How many {note}?: ")) * self.Note_Values[note]
        return self.money_received

    def make_payment(self, cost):
        """Returns True when payment is accepted, or False if insufficient."""
        self.process_coins()
        if self.money_received >= cost:
            change = round(self.money_received - cost, 2)
            print(f"Here is {self.CURRENCY}{change} in change.")
            self.profit += cost
            self.money_received = 0
            return True
        else:
            print("Sorry that's not enough money. Money refunded.")
            self.money_received = 0
            return False
