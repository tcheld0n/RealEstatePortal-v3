class Mortgage:
    def __init__(self, loan_amount, annual_rate, years):
        self._loan_amount = loan_amount
        self._annual_rate = annual_rate
        self._months = years * 12
        self._monthly_payment = self.calculate_monthly_payment()

    # Getter para loan_amount
    @property
    def loan_amount(self):
        return self._loan_amount

    # Setter para loan_amount
    @loan_amount.setter
    def loan_amount(self, value):
        if value <= 0:
            raise ValueError("O valor do empréstimo deve ser positivo.")
        self._loan_amount = value
        self._monthly_payment = self.calculate_monthly_payment()

    # Getter para annual_rate
    @property
    def annual_rate(self):
        return self._annual_rate

    # Setter para annual_rate
    @annual_rate.setter
    def annual_rate(self, value):
        if value < 0:
            raise ValueError("A taxa anual não pode ser negativa.")
        self._annual_rate = value
        self._monthly_payment = self.calculate_monthly_payment()

    # Getter para monthly_payment (somente leitura)
    @property
    def monthly_payment(self):
        return self._monthly_payment

    def calculate_monthly_payment(self):
        rate = self._annual_rate / 100 / 12
        if rate == 0:
            return self._loan_amount / self._months
        return (self._loan_amount * rate) / (1 - (1 + rate) ** -self._months)

    def __str__(self):
        return f"Parcela mensal: R${self._monthly_payment:.2f}"