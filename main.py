class ExpenseTracker:
    def __init__(self, expenses):
        self._expenses = expenses

    def delete(self, item):
        del self._expenses[item]
    
    def filter(self, threshold):
        filtered = {key: value for key, value in self._expenses.items() if value > threshold}
        return filtered

    @property
    def expenses(self):
        return self._expenses
    
# e1 = ExpenseTracker({"Rent": 1200, "Utilities": 400, "Food" : 600, "Necessities" : 100 })

# print(e1.filter(500))