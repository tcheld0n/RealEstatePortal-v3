from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="myGeocoder")

class Property:
    def __init__(self, id, title, description, price, location, property_type, agent, virtual_tour_url=None):
        self._id = id
        self.title = title
        self.description = description
        self.price = price
        self.location = location
        self.property_type = property_type
        self._agent = agent
        self._available = True
        self.virtual_tour_url = virtual_tour_url

    # Utilizando as validações diretamente nos setters
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not value:
            raise ValueError("Título não pode ser vazio.")
        self._title = value

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
    def property_type(self):
        return self._property_type

    @property_type.setter
    def property_type(self, value):
        valid_types = {"sale", "rent"}
        if value not in valid_types:
            raise ValueError(f"Tipo inválido. Use: {valid_types}")
        self._property_type = value

    # Removido os métodos estáticos, pois o validador já está no setter
    def remove_virtual_tour(self):
        self.virtual_tour_url = None

    def update_details(self, **kwargs):
        for attr, value in kwargs.items():
            if hasattr(self, attr):
                setattr(self, attr, value)

    def switch_status(self):
        self._available = not self._available

    # Método para obter coordenadas via geopy (latitude e longitude)
    def get_coordinates(self):
        location = geolocator.geocode(self.location)
        if location:
            return location.latitude, location.longitude
        return None, None

    # Método para gerar o link do Google Maps
    def get_google_maps_link(self):
        latitude, longitude = self.get_coordinates()
        if latitude and longitude:
            return f"https://www.google.com/maps?q={latitude},{longitude}"
        return "Localização não encontrada"

    def to_dict(self):
        return {
            "id": self._id,
            "title": self._title,
            "description": self._description,
            "price": self._price,
            "location": self._location,
            "property_type": self._property_type,
            "agent": self._agent.name,
            "available": self._available,
            "virtual_tour_url": self.virtual_tour_url,
        }

    def __str__(self):
        return (
            f"Propriedade: {self._title}\n"
            f"Descrição: {self._description}\n"
            f"Preço: R${self._price}\n"
            f"Localização: {self._location}\n"
            f"Tipo: {self._property_type}\n"
            f"Disponível: {'Sim' if self._available else 'Não'}\n"
            f"Tour Virtual: {self.virtual_tour_url if self.virtual_tour_url else 'Nenhum'}"
        )