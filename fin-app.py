class FinancialTracker:
    def __init__(self):
        self.income = 0
        self.expenses = 0
        self.balance = -0

    def add_income(self, amount):
        self.balance += amount

    def add_expense(self, amount):
        self.balance -= amount

    def get_balance(self):
        return self.balance

tracker = FinancialTracker()

while True:
    print("What you want to do?")
    print("1. Add an expense")
    print("2. Add a income")
    print("3. Check Balance ")
    answer = float(input("Please select and option: "))

    if answer == 1:
        amount = float(input("Please enter expense amount: "))
        tracker.add_expense(amount)
    elif answer == 2:
        amount = float(input("Please enter the income amount: "))
        tracker.add_income(amount)
    elif answer == 3:
        amount = float(input(f"Your current balance is: {tracker.get_balance()}"))
    elif answer == 4:
        break
    else:
        print("Invalid answer, please select one of the provided options.")
