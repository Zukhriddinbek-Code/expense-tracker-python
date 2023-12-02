def main():
  print(f'🎯 Running Expense Tracker')

  # get user input for expense
  get_user_expense()

  # write the expense to a file
  save_expense_to_file()

  # read file and summarize all the expense 
  summarize_expenses()



def get_user_expense():
  print(f'🎯 Getting User Expense')
  expense_name = input('Enter expense name: ')
  expense_amount = float(input('Enter expense amount: '))
  # print(f'You have entered {expense_name}, {expense_amount}')
  
  #list of categories
  expense_categories = ['🍔 Food', '🏠 Home', '💼 Work', '🎉 Fun', '⺟ Others']

  #user selects a category
  while True:
    print('Select a category: ') 
    for index, value in enumerate(expense_categories):
      print(f'   {index+1}. {value}')

    value_range = f'[1 - {len(expense_categories)}]'
    selected_category = input(f'Enter a category number {value_range}: ')
    break


def save_expense_to_file():
  print(f'🎯 Saving Expense to File')


def summarize_expenses():
  print(f'🎯 Summarize Expenses')


#when we run this as a file, below condition will be true
if __name__ == '__main__':
  main()