# ☕ Day 15 – Coffee Machine Program

## 📝 Project Description

This project simulates a coffee machine that serves three types of coffee: espresso, latte, and cappuccino.  
It interacts with the user, processes coins, manages resources, and handles transactions.

---

## 🚀 Features and Requirements

1. **User Prompt**  
   Asks the user:  
   `What would you like? (espresso/latte/cappuccino):`  
   - Responds based on input  
   - Repeats prompt after each action until turned off  

2. **Turn Off Machine**  
   - When the user inputs `off`, the program stops execution  
   - This is a secret command for maintainers  

3. **Print Report**  
   - When the user inputs `report`, the machine prints the current resources:  
     - Water (ml)  
     - Milk (ml)  
     - Coffee (g)  
     - Money ($)

4. **Resource Check**  
   - Before making a drink, checks if there are enough ingredients  
   - If resources are insufficient, informs the user (e.g. “Sorry there is not enough water.”)  

5. **Process Coins**  
   - Prompts the user to insert coins: quarters ($0.25), dimes ($0.10), nickels ($0.05), pennies ($0.01)  
   - Calculates the total amount inserted  

6. **Transaction Check**  
   - If not enough money, refunds the user and cancels the order  
   - If enough money, adds cost to machine’s profit  
   - If too much money, gives change rounded to 2 decimals  

7. **Make Coffee**  
   - Deducts the ingredients from resources  
   - Confirms with the user: “Here is your latte. Enjoy!” (or espresso/cappuccino)  

---

## 🧪 Example Run

```text
What would you like? (espresso/latte/cappuccino): latte
Please insert coins.
How many quarters? 10
How many dimes? 0
How many nickels? 0
How many pennies? 0
Here is $0.50 dollars in change.
Here is your latte. Enjoy!
What would you like? (espresso/latte/cappuccino): report
Water: 100ml
Milk: 50ml
Coffee: 76g
Money: $2.5
What would you like? (espresso/latte/cappuccino): off
