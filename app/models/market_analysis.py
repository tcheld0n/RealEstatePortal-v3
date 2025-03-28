class MarketAnalysis:
    def __init__(self, property_controller):
        self.property_controller = property_controller  
        self._data = []  

    def add_data(self, data_point):
        self._data.append(data_point)

    def get_average_price(self):
        if not self._data:
            return 0
        return sum(self._data) / len(self._data)

    def analyze_prices_by_location(self, location):
        # Pesquisa propriedades por localização
        properties_in_location = [prop for prop in self.property_controller._properties if prop.location == location]

        if not properties_in_location:
            return None  

        # Cálculo de preços médios, mínimos e máximos
        total_price = sum(prop.price for prop in properties_in_location)
        average_price = total_price / len(properties_in_location)
        min_price = min(properties_in_location, key=lambda x: x.price).price
        max_price = max(properties_in_location, key=lambda x: x.price).price

        return {
            "average_price": average_price,
            "min_price": min_price,
            "max_price": max_price,
            "num_properties": len(properties_in_location)
        }

    def count_properties_by_status(self, location, property_type=None):
        # Conta o número de propriedades disponíveis em um local, podendo filtrar por tipo (venda ou aluguel)
        properties_in_location = [prop for prop in self.property_controller._properties if prop.location == location]

        if property_type:
            properties_in_location = [prop for prop in properties_in_location if prop.property_type == property_type]

        available_properties = [prop for prop in properties_in_location if prop.available]
        return len(available_properties)

    def market_analysis(self, location):
        # Obtém a análise de preços e o número de propriedades disponíveis para venda e aluguel
        price_analysis = self.analyze_prices_by_location(location)
        num_available_sale = self.count_properties_by_status(location, "sale")
        num_available_rent = self.count_properties_by_status(location, "rent")

        if price_analysis:
            print(f"\n===== Análise de Mercado para {location} =====")
            print(f"Preço Médio: R${price_analysis['average_price']:.2f}")
            print(f"Preço Mínimo: R${price_analysis['min_price']:.2f}")
            print(f"Preço Máximo: R${price_analysis['max_price']:.2f}")
            print(f"Número de Propriedades: {price_analysis['num_properties']}")
        else:
            print(f"\nNão há propriedades na localização '{location}'.")

        print(f"\nImóveis Disponíveis para Venda: {num_available_sale}")
        print(f"Imóveis Disponíveis para Aluguel: {num_available_rent}")

    def __str__(self):
        return f"Análise de Mercado: Preço Médio = R${self.get_average_price():.2f}"
