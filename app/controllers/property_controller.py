from app.data.database import db
from app.models.property import Property

class PropertyController:
    def __init__(self):
        self._properties = db.get_properties()

    def add_property(self, property: Property):
        # Verifica se já existe uma propriedade com o mesmo título e localização
        if any(prop.title == property.title and prop.location == property.location for prop in self._properties):
            raise ValueError("Propriedade já cadastrada.")
        db.add_property(property)               # Adiciona a propriedade ao banco de dados
        self._properties = db.get_properties()  # Adiciona a propriedade à lista local
        return property

    def list_properties(self):
        return [vars(prop) for prop in self._properties]

    def find_property_by_id(self, property_id):
        for prop in self._properties:
            if prop.id == property_id:
                return prop
        return None

    def update_property(self, property_id, title=None, description=None, price=None, location=None):
        property_to_update = self.find_property_by_id(property_id)
        if property_to_update:
            property_to_update.update_details(title, description, price, location)
            return property_to_update
        return None

    def delete_property(self, property_id):
        property_to_delete = self.find_property_by_id(property_id)
        if property_to_delete:
            db.properties.remove(property_to_delete)     # Remove do banco de dados
            self._properties.remove(property_to_delete)  # Remove da lista local
            return True
        return False

    def search_all_properties(self):
        return [prop for prop in self._properties]

    def search_property_by_type(self, property_category ):
        return [prop for prop in self._properties if prop.property_category.lower() == property_category.lower()]

    def search_property_by_location(self, location):
        return [prop for prop in self._properties if location.lower() in prop.location.lower()]

    def search_property_by_price_range(self, price_min, price_max):
        return [prop for prop in self._properties if price_min <= prop.price <= price_max]