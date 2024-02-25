
class Category:
    def __init__(self) -> None:
        pass
    def get_balance(self):
        pass
    def deposit(self, amount, description):
        pass
    def withdraw(self, amount, description):
        pass
    def check_balance(self):
        pass
    def transfer(self, amount, destination):
        pass

def create_spend_chart(categories):
    pass

food = budget.Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")

print(food.get_balance())
clothing = budget.Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
auto = budget.Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)

print(food)
print(clothing)

print(create_spend_chart([food, clothing, auto]))