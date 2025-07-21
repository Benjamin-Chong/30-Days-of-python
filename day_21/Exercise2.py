class PersonAccount:
    def __init__(self, firstname, lastname, incomes = None, expenses = None):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = incomes if incomes is not None else []
        self.expenses = expenses if expenses is not None else []

    def add_income(self, name, amount):
        self.incomes.append((name, amount))

    def add_expense(self, name, amount):
        self.expenses.append((name, amount))
    
    def total_inc(self):
        total = sum(amount for amount, amount in self.incomes)
        return total
    
    def total_expen(self):
        total = sum(amount for amount, amount in self.expenses)
        return total
    
    def account_balance(self):
        return self.total_inc() - self.total_expen()

    def account_info(self):
        return f'{self.firstname} {self.lastname} has a total income of {self.total_inc()} and total expenses of {self.total_expen()}. Their balance is {self.account_balance()}'
    
#Example Usage:
pa = PersonAccount('Owen', 'Smith')
pa.add_income('salary', 3000)
pa.add_income('freelance', 800)
pa.add_expense('rent', 1200)
pa.add_expense('groceries', 400)

print(pa.account_info())
