class Category:
  
  def __init__(self, type):
    self.type = type
    self.ledger = []
    self.total_amount = 0
  
  def deposit(self, amount, description = ""):
    self.total_amount += amount
    info = {"amount": amount, "description":description}
    self.ledger.append(info)
  
  def withdraw(self, amount, description = ""):
    if self.check_funds(amount):
      amount = amount * (-1)
      self.total_amount += amount
      info = {"amount": amount, "description":description}
      self.ledger.append(info)
      return True
    else:
      return False

  def get_balance(self):
    return self.total_amount
    
  def transfer(self, amount, type):
    if type != None:
      if self.check_funds(amount):
        withdraw_description = "Transfer to {0}".format(type.type)
        self.withdraw(amount, withdraw_description)
    
        deposit_description = "Transfer from {0}".format(self.type)
        type.deposit(amount, deposit_description)
        
        return True 
      else:
        return False

  def check_funds(self, amount):
    if self.total_amount - amount < 0:
      return False
    else:
      return True

  def __str__(self):
    overall = ""
    header = ""
    total = ""

    # create header
    for i in range(30 - len(self.type) + 1):
      if i == (30 - len(self.type)) // 2:
        header += self.type
      else:
        header += '*'

    overall += header + '\n'        
        
    # create list text
    for list in self.ledger:
      list_text = ""
      list_amount = str(list["amount"])
      list_description = list["description"]
      category_total_amount = str(round(self.total_amount, 2))
      
      if not list_amount.count('.'):
        list_amount += '.00'
      
      for j in range(23 + (7 - len(list_amount))):
        if j < len(list_description) and j < 23:
          list_text += list_description[j]
        else:
          list_text += " "
 
      list_text += list_amount

      overall += list_text + '\n'

    #  create total text
    if not category_total_amount.count('.'):
        category_total_amount += '.00'
      
    total += "Total: {0}".format(category_total_amount)
    
    overall += total

    return overall

def create_spend_chart(categories):
  total_spend = 0
  max_length_str = 0
  percentage = []
  type_names = []
  total_spend = 0
  total_category_spend = []
  
  # calculate total spend
  for category in categories:
    names = []
    overall = ""

    # calculate total spend
    for list_ledger in category.ledger:
      list_ledger_amount = int(list_ledger["amount"])
      if list_ledger_amount < 0:
        total_category_spend.append(list_ledger_amount * (-1))
        total_spend += list_ledger_amount * (-1)
    
    # find maximun length of type name
    if len(category.type) > max_length_str:
      max_length_str = len(category.type)

    for letter in category.type:
      names.append(letter)

    type_names.append(names)
    
  # calculate percentage
  for category_spend in total_category_spend:  
    category_percentage = round((category_spend / total_spend) * 100) / 10
    percentage.append(category_percentage)

  # add header
  overall += "Percentage spent by category\n"

  # bar limit
  bar = 100

  # loop though each line
  for i in range(10):
    current_bar = str(bar - (i * 10))
    current_line = ""
    
    for j in range(3 - len(current_bar)):
      current_line += " "
      
    current_line += "{0}| ".format(current_bar)
    
    for list_percentage in percentage:
      if 10 - i <= list_percentage:
        current_line += "o  "
      else:
        current_line += "   "
    
    overall += current_line + "\n"

  # add last bar
  overall += "  0| o  o  o  \n"

  # add break line
  break_line = ""
  for k in range((len(categories) * 3) + 4 + 1):
    if k > 3:
      break_line += "-"
    else:
      break_line += " "
      
  overall += break_line + "\n"

  # add category
  for l in range(max_length_str):
    category_line = "     "
    for name in type_names:
      if l < len(name):
        category_line += name[l] + "  "
      else:
        category_line += "   "

    if l == max_length_str - 1:
      overall += category_line
    else:
      overall += category_line + "\n"

  return overall
