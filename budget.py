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
    amount = amount * (-1)
    
    if self.check_fund(amount):
      self.total_amount += amount
      info = {"amount": amount, "description":description}
      self.ledger.append(info)
    else:
      raise ValueError('insufficient fund')
      return False

  def get_balance(self):
    return self.total_amount
    
  def transfer(self, amount, type):
    if self.check_fund(amount):
      withdraw_description = "Transfer to [{0}]".format(type.type)
      self.withdraw(amount, withdraw_description)
  
      deposit_description = "Transfer From [{0}]".format(self.type)
      type.deposit(amount, deposit_description)

  def check_fund(self, amount):
    if amount > self.total_amount:
      return False
    else:
      return True


# def create_spend_chart(categories):
