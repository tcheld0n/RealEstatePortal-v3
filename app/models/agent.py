from app.models.user import User

class Agent(User):
    def __init__(self, user_id, name, email, password):
        super().__init__(user_id, name, email, password)
        self._properties = []

    def add_property(self, property):
        self._properties.append(property)

    def list_properties(self):
        return self._properties

    def get_role(self):
        return "Agente"
