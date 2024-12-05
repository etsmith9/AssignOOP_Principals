#question 1 - You are required to build a Personal Budget Management application. 
# The application will manage budget categories like food, entertainment, 
# utilities, etc., ensuring that budget details remain private and are accessed 
# or modified through public methods.

#Task 1: Define Budget Category Class Create a class `BudgetCategory`
#  with private attributes for category name and allocated budget. 
# - Initialize these attributes in the constructor.
# - Expected Outcome: A `BudgetCategory` class capable of storing 
# category details securely.

#Task 2: Implement Getters and Setters - Write getter and setter methods 
# for both the category name and the allocated budget. 
# - Ensure that the setter methods include validation 
# (e.g., budget should be a positive number).
#Expected Outcome: Methods that allow controlled access and modification 
# of the private attributes, with validation checks in place.

#Task 3: Add Budget Functionality Implement a method to add expenses 
# to a category and adjust the budget accordingly. 
# - Validate the expense amount before making deductions from the budget.
# Expected Outcome: Ability to track expenses per 
# category and update the remaining budget safely.

#Task 4: Display Budget Details Create a method to display the details of 
# a budget category, including the name, allocated budget, and 
# remaining budget after expenses.
#Expected Outcome: Users can view a summary of each 
# budget category, showcasing encapsulation in action.

class BudgetCategory:
    def __init__(self, category_name, allocated_budget):
        self.__category_name = category_name
        self.__allocated_budget = allocated_budget
        self.__expenses = 0

    def get_category_name(self):
        return self.__category_name
    
    def set_category_name(self, category_name):
        self.__category_name = category_name
    
    def get_allocated_budget(self):
        return self.__allocated_budget
    
    def set_allocated_budget(self, allocated_budget):
        if allocated_budget < 0:
            print("Error: Budget cannot be negative!")
        else:
            self.__allocated_budget = allocated_budget

    def add_expense(self, amount):
        if amount < 0: 
            print("Error: Expense cannot be negative.")
        else: 
            self.__expenses += amount
            if self.__expenses > self.__allocated_budget:
                print(f"Warning: You have exceeded your budget by ${self.__expenses - self.__allocated_budget}.")
            else:
                print(f"Expense of ${amount} added. Total expenses: ${self.__expenses}")

    def display_category_summary(self):
        remaining_budget = self.__allocated_budget - self.__expenses
        print(f"Category: {self.__category_name}")
        print(f"Allocated Budget: ${self.__allocated_budget}")
        print(f"Total Expenses:  ${self.__expenses}")
        print(f"Remaining Budget:  ${remaining_budget}")

    def display_budget_details(self):
        remaining_budget = self.__allocated_budget - self.__expenses
        print(f"Budget Category: {self.__category_name}")
        print(f"Allocated Budget: ${self.__allocated_budget}")
        print(f"Remaining Budget: ${remaining_budget}")

if __name__ == "__main__":

    food_category = BudgetCategory("Food", 500)
    food_category.display_budget_details()
    food_category.add_expense(100)
    food_category.add_expense(300)
    food_category.display_budget_details()
    food_category.add_expense(-50)
    food_category.add_expense(300)
    food_category.display_budget_details()

    utilities_category = BudgetCategory("Utilities", 600)
    utilities_category.display_budget_details()
    utilities_category.add_expense(400)
    utilities_category.display_budget_details()