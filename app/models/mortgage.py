class Mortgage:
    def __init__(self, loan_amount, annual_rate, years):
        # Validação básica das entradas
        if loan_amount <= 0:
            raise ValueError("O valor do empréstimo deve ser positivo.")
        if annual_rate < 0:
            raise ValueError("A taxa anual não pode ser negativa.")
        if years <= 0:
            raise ValueError("O prazo deve ser positivo.")

        # Atribui os valores diretamente
        self.loan_amount = loan_amount
        self.annual_rate = annual_rate
        self.years = years

        # Calcula os valores iniciais
        self.months = years * 12
        self.monthly_payment = self._calculate_monthly_payment()
        self.total_payment = self._calculate_total_payment()

    def _calculate_monthly_payment(self):
        rate = self.annual_rate / 100 / 12
        if rate == 0:
            return self.loan_amount / self.months
        return (self.loan_amount * rate) / (1 - (1 + rate) ** -self.months)

    def _calculate_total_payment(self):
        return self.monthly_payment * self.months

    def __str__(self):
        return (
            f"Parcela mensal: R${self.monthly_payment:.2f}\n"
            f"Total a ser pago: R${self.total_payment:.2f}"
        )