from app.models.mortgage import Mortgage

class MortgageController:
    def __init__(self):
        self.calculations = []

    def calculate_mortgage(self, loan_amount, annual_rate, years):
        calculator = Mortgage(loan_amount, annual_rate, years)
        self.calculations.append(calculator)
        return calculator

    # def get_monthly_payment(self, calculator):
    #     return calculator.monthly_payment
    #
    # def simulate_payment(self, loan_amount, annual_rate, years):
    #     # Simula o pagamento sem salvar a instância
    #     calculator = Mortgage(loan_amount, annual_rate, years)
    #     return calculator.monthly_payment
