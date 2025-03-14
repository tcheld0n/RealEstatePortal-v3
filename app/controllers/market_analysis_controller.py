from app.models.market_analysis import MarketAnalysis
from app.data.database import db

class MarketAnalysisController:
    def __init__(self, property_controller):
        self.property_controller = property_controller
        # Passando o property_controller para a instância do MarketAnalysis
        self.market_analysis = MarketAnalysis(self.property_controller)

    def get_market_analysis(self, location):
        # Filtrando as propriedades pela localização
        propriedades_na_localizacao = [prop for prop in db.get_properties() if
                                       prop.location.lower() == location.lower()]

        if not propriedades_na_localizacao:
            return None

        # Calculando preço médio
        precos = [prop.price for prop in propriedades_na_localizacao]
        preco_medio = sum(precos) / len(precos)

        # Contando número de imóveis para venda e aluguel
        num_venda = sum(1 for prop in propriedades_na_localizacao if prop.property_type == "sale")
        num_aluguel = sum(1 for prop in propriedades_na_localizacao if prop.property_type == "rent")

        # Retorna a análise de mercado
        return {
            "Preço Médio": preco_medio,
            "Propriedades à venda": num_venda,
            "Propriedades para aluguel": num_aluguel
        }