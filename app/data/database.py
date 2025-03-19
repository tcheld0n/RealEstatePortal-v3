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
        self._next_property_id = 1

        # Inicializa os dados do banco de dados
        self.initialize_data()

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
        # Verifica se já existe uma propriedade com o mesmo título e localização
        if any(prop.title == property.title and prop.location == property.location for prop in self.properties):
            raise ValueError("Propriedade já cadastrada.")

        property._id = self._next_property_id
        self.properties.append(property)
        self._next_property_id += 1

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

    # Database inicial de propriedades
    def initialize_data(self):
        # Propriedades predefinidas
        properties = [
            Property(
                id=1,
                title="Casa na Praia",
                description="Linda casa com vista para o mar",
                price=1000000,
                location="Rio de Janeiro",
                property_category="Casa",
                transaction_type="Venda",
                agent="João Silva"
            ),
            Property(
                id=2,
                title="Apartamento no Centro",
                description="Apartamento moderno",
                price=500000,
                location="São Paulo",
                property_category="Apartamento",
                transaction_type="Aluguel",
                agent="Maria Souza"
            ),
            Property(
                id=3,
                title="Terreno Residencial",
                description="Terreno plano e amplo",
                price=300000,
                location="Belo Horizonte",
                property_category="Terreno",
                transaction_type="Venda",
                agent="Carlos Oliveira"
            )
        ]

        # Adiciona as propriedades ao banco de dados
        for prop in properties:
            self.add_property(prop)

# Instância global do banco de dados para ser usada em todo o sistema
db = Database()