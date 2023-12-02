from expense import Expense


def main():
  print(f'🎯 Running Expense Tracker')

  # get user input for expense
  expense = get_user_expense()

  # write the expense to a file
  save_expense_to_file()

  # read file and summarize all the expense 
  summarize_expenses()



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



def save_expense_to_file():
  print(f'🎯 Saving Expense to File')


def summarize_expenses():
  print(f'🎯 Summarize Expenses')


#when we run this as a file, below condition will be true
if __name__ == '__main__':
  main()