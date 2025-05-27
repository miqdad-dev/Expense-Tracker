class Expense:    
    def __init__(self, name, amount, category, date):
        self.name = name
        self.amount = amount
        self.category = category
        self.date = date

    def __str__(self):
        return f"{self.name} - ${self.amount} | {self.category} on {self.date}"

expenses = []

categories = ("food","transport","shopping","bills", "others")


def add_expense(name, amount, date, category):
    new_expense = Expense(name, float(amount), category, date)
    expenses.append(new_expense)

def view_expenses():
   for expense in expenses:
      print(expense) 

def view_total():
    total = sum(item.amount for item in expenses)
    return total
    
def show_category():
    all_categories = set(item.category for item in expenses)
    return all_categories
    
    
def show_ByDate(date):
   for item in expenses:
    if item.date == date:
        print(item)
    
def delete_expense(name):
    for i in range(len(expenses)):
     if expenses[i].name == name:
        del expenses[i]
        return True
    return False



while True:
    print("\nChoose an option:")
    print("1. Add Expense")
    print("2. View All Expense")
    print("3. View Total Spent")
    print("4. View by Categories")
    print("5. View by Date")
    print("6. Delete Expense")
    print ("7. Exit")
    
    option = int(input("Choose an Option between (1 to 7): "))
       
    if option == 1:
        name = input("Enter an Item name: ")
        try:
            amount = float(input("Whats the amount "))
        except ValueError:
            print("Enter a valid number (1 to 7).")
            continue
        date = input("Enter date (e.g. 2024-05-26): ")
        print(f"Pick from ", categories)
        pick_category = input("Pick from above: ")
        if pick_category in categories:
            add_expense(name, amount, date, pick_category)
            print("Item added successfully")
        else:
            print("Invalid category. Item not added.")
   
    elif option == 2:
        if expenses:
            view_expenses()
        else:
                print("No expense yet.")
    elif option == 3:
        print(f"Total Spent: ${view_total()}")

    elif option == 4:
        print("Categories used so far: ", show_category())
        category = input("Pick a Category: ").lower()
        found = False
        for item in expenses:
            if item.category == category:
                print(item)
                found = True
        if not found:
               print("No expenses found in that category.")
        
    elif option == 5:
        date = input("Enter date to filter (e.g. 2024-05-26): ")
        print("Expenses on", date + ":")
        show_ByDate(date)
           
        
    elif option == 6:
        expense_name = input("Enter the name of the expense to delete: ")
        if delete_expense(expense_name):
            print("Expense deleted successfully.")
        else:
                print("Expense not found.")

      
    elif option == 7:
        print("Exiting app. Goodbye!")
        break

    else:
        print("Invalid choice. Enter a number between 1 and 7.")

    input("\nPress Enter to continue...")

    

    
