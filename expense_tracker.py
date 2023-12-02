def main():
  print(f'🎯 Running Expense Tracker')

  # get user input for expense
  get_user_expense()

  # write the expense to a file
  save_expense_to_file()

  # read file and summarize all the expense 
  summarize_expenses()
  pass


def get_user_expense():
  print(f'🎯 Getting User Expense')
  pass

def save_expense_to_file():
  print(f'🎯 Saving Expense to File')
  pass

def summarize_expenses():
  print(f'🎯 Summarize Expenses')
  pass

#when we run this as a file, below condition will be true
if __name__ == '__main__':
  main()