from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="myGeocoder")

class Property:
    def __init__(self, id, title, description, price, location, property_category, transaction_type, agent, virtual_tour_url=None):
        self._id = id
        self.title = title
        self.description = description
        self.price = price
        self.location = location
        self.property_category = property_category
        self.transaction_type = transaction_type
        self._agent = agent
        self._available = True
        self.virtual_tour_url = virtual_tour_url

    # Validações e getters/setters
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not value:
            raise ValueError("Título não pode ser vazio.")
        self._title = value

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        if not value:
            raise ValueError("Descrição não pode ser vazia.")
        self._description = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Preço não pode ser negativo.")
        self._price = value

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, value):
        if not value:
            raise ValueError("Localização não pode ser vazia.")
        self._location = value

    @property
    def property_category(self):
        return self._property_category

    @property_category.setter
    def property_category(self, value):
        valid_categories = {"Casa", "Apartamento", "Terreno"}
        if value not in valid_categories:
            raise ValueError(f"Categoria inválida. Use: {valid_categories}")
        self._property_category = value

    @property
    def transaction_type(self):
        return self._transaction_type

    @transaction_type.setter
    def transaction_type(self, value):
        valid_transactions = {"Venda", "Aluguel"}
        if value not in valid_transactions:
            raise ValueError(f"Transação inválida. Use: {valid_transactions}")
        self._transaction_type = value

    # Ajuste para acessar o ID
    @property
    def id(self):
        return self._id

    @property
    def agent(self):
        return self._agent

    @agent.setter
    def agent(self, value):
        if not value:
            raise ValueError("Agente não pode ser vazio.")
        self._agent = value

    @property
    def available(self):
        return self._available

    @available.setter
    def available(self, value):
        if not isinstance(value, bool):
            raise ValueError("Disponibilidade deve ser um valor booleano.")
        self._available = value

    @property
    def virtual_tour_url(self):
        return self._virtual_tour_url

    @virtual_tour_url.setter
    def virtual_tour_url(self, value):
        self._virtual_tour_url = value

    def remove_virtual_tour(self):
        self.virtual_tour_url = None

    def update_details(self, **kwargs):
        for attr, value in kwargs.items():
            if hasattr(self, attr):
                setattr(self, attr, value)

    def switch_status(self):
        self._available = not self._available

    def get_coordinates(self):
        location = geolocator.geocode(self.location)
        if location:
            return location.latitude, location.longitude
        return None, None

    def get_google_maps_link(self):
        latitude, longitude = self.get_coordinates()
        if latitude and longitude:
            return f"https://www.google.com/maps?q={latitude},{longitude}"
        return "Localização não encontrada"

    def __str__(self):
        return (
            f"ID: {self._id}\n"
            f"Propriedade: {self._title}\n"
            f"Descrição: {self._description}\n"
            f"Preço: R${self._price}\n"
            f"Localização: {self._location}\n"
            f"Categoria: {self._property_category}\n"
            f"Transação: {'Venda' if self._transaction_type == 'Venda' else 'Aluguel'}\n"
            f"Disponível: {'Sim' if self._available else 'Não'}\n"
            f"Tour Virtual: {self.virtual_tour_url if self.virtual_tour_url else 'Nenhum'}\n"
        )