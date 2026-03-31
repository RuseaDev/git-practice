class ExpenseTracker:
    def __init__(self, expenses):
        self._expenses = expenses

    @property
    def expenses(self):
        return self._expenses
    
ExT = ExpenseTracker([5,10,14])

print(ExT.expenses)