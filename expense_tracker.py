from expense import Expense
import calendar
import datetime


def main():
  print(f'🎯 Running Expense Tracker')
  expense_file_path = 'expenses.csv'
  budget = 2000

  # get user input for expense
  expense = get_user_expense()

  # write the expense to a file
  save_expense_to_file(expense, expense_file_path)

  # read file and summarize all the expense 
  summarize_expenses(expense_file_path, budget)



def get_user_expense():
  print(f'🎯 Getting User Expense')
  expense_name = input('Enter expense name: ')
  expense_amount = float(input('Enter expense amount: '))
  expense_categories = ['🍔 Food', '🏠 Home', '💼 Work', '🎉 Fun', '⺟ Others']

  #user selects a category
  while True:
    print('Select a category: ') 
    for index, value in enumerate(expense_categories):
      print(f'   {index+1}. {value}')

    value_range = f'[1 - {len(expense_categories)}]'
    selected_index = int(input(f'Enter a category number {value_range}: ')) - 1

    if selected_index in range(len(expense_categories)):
      selected_category = expense_categories[selected_index]
      new_expense = Expense(name=expense_name, category=selected_category, amount=expense_amount)
      return new_expense
    else:
      print(f'Invalid category selected. Please try again!')


#type hint for editor to know what is inside Expense class and suggest its constructors
def save_expense_to_file(expense: Expense, expense_file_path):
  print(f'🎯 Saving Expense to File: {expense} to {expense_file_path}')
  with open(expense_file_path, 'a') as f:
    f.write(f'{expense.name}, {expense.amount}, {expense.category}\n')


def summarize_expenses(expense_file_path, budget):
  print(f'🎯 Summarize Expenses')
  expenses: list[Expense] = [] #expense is Expense object type hint
  with open(expense_file_path, 'r') as f:
    lines = f.readlines()
    for line in lines:
      #strip returns a string leading and trailing whitespace removed
      expense_name, expense_amount, expense_category = line.strip().split(',') #destructure right away
      line_expense = Expense(name=expense_name, category=expense_category, amount=float(expense_amount))
      expenses.append(line_expense)
  
  amount_by_category = {}
  for expense in expenses:
    key = expense.category
    if key in amount_by_category:
      amount_by_category[key] += expense.amount
    else: 
      amount_by_category[key] = expense.amount
  
  print('Expenses By Category 📈')
  for key, amount in amount_by_category.items():
    print(f'   {key}: ${amount:.2f} ')
  
  total_spent = sum([x.amount for x in expenses])
  remaining_budget = budget - total_spent

  #printing total expense and remaining budget
  print(f'💵 Total Spent: ${total_spent:.2f}')
  print(f'✅ Remaining Budget: ${remaining_budget:.2f}')

  # get the current date
  now = datetime.datetime.now()
  #get the number of days in the current month
  days_in_month = calendar.monthrange(now.year, now.month)[1]
  # calculate the remaining number of days in current month
  remaining_days = days_in_month - now.day

  #divide remaining budget into remaining days and get the amount to be spent throughout rest of month
  daily_budget = remaining_budget / remaining_days
  print(green(f'👉 Budget Per Day: ${daily_budget:.2f}'))
  
#turns string into green color
def green(text):
  return f'\033[92m{text}\033[0m'

#when we run this as a file, below condition will be true
if __name__ == '__main__':
  main()