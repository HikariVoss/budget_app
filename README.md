# budget_app
## freecodecamp challenge: budget app

Complete the `Category` class in `budget.py.` It should be able to instantiate objects based on different budget categories like food, clothing, and entertainment. When objects are created, they are passed in the name of the category. The class should have an instance variable called `ledger` that is a list. The class should also contain the following methods:

- A `deposit` method that accepts an amount and description. If no description is given, it should default to an empty string. The method should append an object to the ledger list in the form of `{"amount": amount, "description": description}`.
- A `withdraw` method that is similar to the `deposit` method, but the amount passed in should be stored in the ledger as a negative number. If there are not enough funds, nothing should be added to the ledger. This method should return `True` if the withdrawal took place, and `False` otherwise.
- A `get_balance` method that returns the current balance of the budget category based on the deposits and withdrawals that have occurred.
- A `transfer` method that accepts an amount and another budget category as arguments. The method should add a withdrawal with the amount and the description "Transfer to [Destination Budget Category]". The method should then add a deposit to the other budget category with the amount and the description "Transfer from [Source Budget Category]". If there are not enough funds, nothing should be added to either ledgers. This method should return `True` if the transfer took place, and `False` otherwise.
- A `check_funds` method that accepts an amount as an argument. It returns `False` if the amount is greater than the balance of the budget category and returns `True` otherwise. This method should be used by both the withdraw `method` and transfer `method`.

When the budget object is printed it should display:

- A title line of 30 characters where the name of the category is centered in a line of `*` characters.
- A list of the items in the ledger. Each line should show the description and amount. The first 23 characters of the description should be displayed, then the amount. The amount should be right aligned, contain two decimal places, and display a maximum of 7 characters.
- A line displaying the category total.
Here is an example of the output:

```
*************Food*************
initial deposit        1000.00
groceries               -10.15
restaurant and more foo -15.89
Transfer to Clothing    -50.00
Total: 923.96
```

Besides the `Category` class, create a function (outside of the class) called `create_spend_chart` that takes a list of categories as an argument. It should return a string that is a bar chart.

The chart should show the percentage spent in each category passed in to the function. The percentage spent should be calculated only with withdrawals and not with deposits. Down the left side of the chart should be labels 0 - 100. The "bars" in the bar chart should be made out of the "o" character. The height of each bar should be rounded down to the nearest 10. The horizontal line below the bars should go two spaces past the final bar. Each category name should be written vertically below the bar. There should be a title at the top that says "Percentage spent by category".

This function will be tested with up to four categories.

Look at the example output below very closely and make sure the spacing of the output matches the example exactly.

### Percentage spent by category
```
100|          
 90|          
 80|          
 70|          
 60| o        
 50| o        
 40| o        
 30| o        
 20| o  o     
 10| o  o  o  
  0| o  o  o  
    ----------
     F  C  A  
     o  l  u  
     o  o  t  
     d  t  o  
        h     
        i     
        n     
        g     
```

## My solution 

### plan
For this challenge I'm going to use OOP to create object with a methods to deposit money into a category, withdraw money/spend money from a category, as well as a method to transfer money from one category to another, and a `check_funds` method which is called by `withdraw` and `transfer` method
Finally out side of the class Im going to make a fucntion that takes the object and prints out a bar chart with spending per category

### Goal
The aim of this challenge is to get better at Object Oriented Programming, which is a weak point of mine

### Main tests

```
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
```

### 1st main commit 
So far I have learned how to use basic funcitonallity of classes in python, such as making custom methods and magic methods; specifically the `__init__()` and `__str__` methods. Most of the fuctionallity has been added: the only main functionallity I have not started on is the transfer method, and the spend chart function (outside the `Category` class)
Plan for the transfer method
For the transfer level I will use a total balance on a class level, then transfer money from instance to class and then to the destination instance.
Plan for the spend chart function
The spend chart function will take in instance and spit out a chart, fairly simple I think, hopefully this doesn't jinks me.

### Final build

I struggled a lot to make the transfer method, because i was trying to assign the transactions to a class variable and the create a for loop for all the other methods that iterates through the `transactions` class variable. 
However there is a much simpler way: I just called the destination instance within the transfer method.
The spend chart did turn out to be quite simple just requires several loops to get it working.

### Output from the [above tests](https://github.com/HikariVoss/budget_app?tab=readme-ov-file#main-tests)

```
973.96
*************Food*************
initial deposit        1000.00
groceries               -10.15
restaurant and more foo -15.89
Transfer to Clothing    -50.00
Total: 923.96
***********Clothing***********
Transfer from Food       50.00
                        -25.55
Total: 24.45
Percentage spent by category
100|
 90|
 80|
 70|
 60| o 
 50| o 
 40| o 
 30| o 
 20| o  o 
 10| o  o  o 
  0| o  o  o 
    ---------
     F  C  A 
     o  l  u 
     o  o  t 
     d  t  o 
        h    
        i    
        n    
        g    
```

### Useful resources 

I used this [OOP tutorial from freecodecamp](https://youtu.be/Ej_02ICOIgs?si=gQS1jDAwbsp52AnO) and the official python docs. 