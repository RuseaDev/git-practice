class ExpenseTracker:
    def __init__(self, expenses):
        self._expenses = expenses

    @property
    def expenses(self):
        return self._expenses
    
    def add(self, item):
        return self._expenses.append(item)
    
ExT = ExpenseTracker([5,10,14])

ExT.add(2)
print(ExT.expenses)

