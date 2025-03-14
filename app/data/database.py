# Simulação de Banco de Dados em Memória
from app.models.user import User
from app.models.property import Property
from app.models.visit import Visit
from app.models.review import Review

class Database:
    def __init__(self):
        self.users = []         # Lista de usuários (Clientes e Agentes)
        self.properties = []    # Lista de propriedades
        self.visits = []        # Lista de visitas agendadas
        self.reviews = []       # Lista de avaliações

    # Adiciona um novo usuário à lista
    def add_user(self, user: User):
        self.users.append(user)

    # Retorna todos os usuários na lista
    def get_users(self):
        return self.users

    # Retorna apenas os clientes
    def get_clients(self):
        return [user for user in self.users if user.user_type == "Cliente"]

    # Retorna apenas os agentes
    def get_agents(self):
        return [user for user in self.users if user.user_type == "Agente"]

    # Adiciona uma propriedade
    def add_property(self, property: Property):
        self.properties.append(property)

    # Retorna todas as propriedades
    def get_properties(self):
        return self.properties

    # Adiciona uma visita
    def add_visit(self, visit: Visit):
        self.visits.append(visit)

    # Retorna todas as visitas
    def get_visits(self):
        return self.visits

    # Adiciona uma avaliação
    def add_review(self, review: Review):
        self.reviews.append(review)

    # Retorna todas as avaliações
    def get_reviews(self):
        return self.reviews

# Instância global do banco de dados para ser usada em todo o sistema
db = Database()