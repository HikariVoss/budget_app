import math

class Category:
    total_balance = 0
    def __init__(self, category) -> None:
        self.category = category
        self.transactions = []
        self.balance = 0
        self.spending = 0
    
    def __str__(self) -> str: 
        self.string = ''

        # format title
        self.title_len = len(self.category)
        self.space_left = self.num_to_char(math.floor((30 - self.title_len) / 2), '*')
        self.space_right = self.num_to_char(math.ceil((30 - self.title_len) / 2), '*')
        self.string = f'{self.space_left}{self.category}{self.space_right}'

        # format transactions
        for transaction in self.transactions: 
            self.amount, self.description = transaction
            self.amount_len = len(str(self.amount))
            self.description_len = len(str(self.description))
            self.white_space = 29 - self.amount_len - self.description_len
            if self.white_space < 0:
                self.description = self.description[:self.white_space]
            self.string += f'\n{self.description}{self.num_to_char(self.white_space, " ")} {self.amount}'
        
        # format total
        self.string += f'\nTotal: {self.balance:.2f}'
        return self.string
    
    def get_balance(self):
        return self.balance
    
    def deposit(self, amount, description):
        self.balance += amount
        self.transactions.append([f'{amount:.2f}', description])
    
    def withdraw(self, amount, description = ''):
        if self.check_balance(amount):
            self.balance -= amount
            self.transactions.append([f'{-amount:.2f}', description])
            self.spending = amount
    
    def transfer(self, amount, destination):
        if self.check_balance(amount):
            self.balance -= amount
            self.spending += amount
            self.transactions.append([f'{-amount:.2f}', f'Transfer to {destination.category}'])
            destination.recieve_transfer(amount, self.category)
        
    def recieve_transfer(self, amount, origin):
        self.balance += amount
        self.transactions.append([f'{amount:.2f}', f'Transfer from {origin}'])
        
    def check_balance(self, amount):
        if (self.balance - amount) >= 0:
            return True
        else: return False
    
    def num_to_char(self, num, char = ' '):
        self.chars = ''
        for i in range(0, num):
            self.chars += char
        return self.chars
    
def create_spend_chart(categories):
    total = 0
    spending = []
    for category in categories:
        total += category.spending
    for cat in categories:
        percentage = math.floor((cat.spending / total) * 10)
        spending.append([cat.category, percentage])
    # spending chart title
    string = f'Percentage spent by category\n'
    longest_category = 0
    for category in spending: 
        if len(category[0]) > longest_category:
            longest_category = len(category[0])
    # spending chart
    line = 10
    while line >= 0:
        chars = f'{line * 10}|'
        if len(chars) == 2:
            string += f'  {chars}'
        elif len(chars) == 3:
            string += f' {chars}'
        else: 
            string += f'{chars}'
        for category in spending:
            if category[1] >= line:
                string += f' o '
        string += f'\n'
        line -= 1
    # divider line
    string += '    '
    for category in spending: 
        string += '---'
    string += '\n'
    for i in range(0, longest_category):
        string += '    '
        for category in spending:
            try: 
                string += f' {category[0][i]} '
            except: 
                string += '   '
        string += '\n'
        longest_category -= 1
    return string

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