from app.models.mortgage import Mortgage

class MortgageController:
    def calculate_mortgage(self, loan_amount, annual_rate, years):
        calculator = Mortgage(loan_amount, annual_rate, years)
        return calculator