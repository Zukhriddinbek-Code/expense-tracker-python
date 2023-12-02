from expense import Expense


def main():
  print(f'🎯 Running Expense Tracker')
  expense_file_path = 'expenses.csv'

  # get user input for expense
  expense = get_user_expense()

  # write the expense to a file
  save_expense_to_file(expense, expense_file_path)

  # read file and summarize all the expense 
  summarize_expenses(expense_file_path)



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


def summarize_expenses():
  print(f'🎯 Summarize Expenses')


#when we run this as a file, below condition will be true
if __name__ == '__main__':
  main()