class MarketAnalysisController:
    def __init__(self, property_controller):
        self.property_controller = property_controller

    def get_market_analysis(self, location):
        # Obtém todas as propriedades na localização selecionada
        properties = self.property_controller.search_property_by_location(location)

        if not properties:
            return None

        # Filtra propriedades à venda e para aluguel
        properties_for_sale = [p for p in properties if p.transaction_type == "Venda"]
        properties_for_rent = [p for p in properties if p.transaction_type == "Aluguel"]

        # Calcula o preço médio
        total_price = sum(p.price for p in properties)
        avg_price = total_price / len(properties)

        # Conta o número de propriedades à venda e para aluguel
        num_sale = len(properties_for_sale)
        num_rent = len(properties_for_rent)

        return {
            "avg_price": avg_price,
            "num_sale": num_sale,
            "num_rent": num_rent     
        }