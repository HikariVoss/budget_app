import math

class Category:
    def __init__(self, category) -> None:
        self.category = category
        self.transactions = []
        self.balance = 0
    def __str__(self) -> str:
        self.string = ''
        # format title
        self.title_len = len(self.category)
        self.white_space_left = math.floor((30 - self.title_len) / 2)
        
        self.white_space_right = math.ceil((30 - self.title_len) / 2)
        
        self.string = f'{self.num_to_char(self.white_space_left, "*")}{self.category}{self.num_to_char(self.white_space_right, "*")}'
        for i in self.transactions: 
            pass

        return self.string
    def get_balance(self):
        return self.balance
    
    def deposit(self, amount, description):
        if self.check_balance(amount):
            self.transactions.append([amount, description])
    
    def withdraw(self, amount, description = ''):
        self.transactions.append([-amount, description])
    
    def transfer(self, amount, destination):
        pass
    
    def check_balance(self, amount):
        if (self.balance + amount) >= 0:
            return True
        else: return False
    
    def num_to_char(self, num, char = ' '):
        self.chars = ''
        for i in range(0, num):
            self.chars += char
        return self.chars
    
def create_spend_chart(categories):
    pass


food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")

print(food.get_balance())
clothing = Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
auto = Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)

print(food)
print(clothing)

print(create_spend_chart([food, clothing, auto]))