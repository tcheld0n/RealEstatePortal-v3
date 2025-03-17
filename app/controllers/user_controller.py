from app.data.database import db
from app.models.agent import Agent
from app.models.client import Client
from app.models.user import User

class UserController:
    def login(self):
        email = input("Digite seu email: ")
        password = input("Digite sua senha: ")

        # Procura o usuário com o email e senha correspondentes
        user = next((user for user in db.get_users() if user.email == email and user.password == password), None)

        if user:
            print(f"Login realizado com sucesso! Bem-vindo, {user.name}.")
            return user  # Retorna o usuário logado
        else:
            print("Erro: Email ou senha incorretos.")
            return None

    # Cadastra um novo usuário
    def register_user(self, name, email, password, user_type):
        # Valida o tipo de usuário
        valid_types = ["Cliente", "Agente"]
        if user_type.capitalize() not in valid_types:
            print(f"Erro: Tipo de usuário inválido. Escolha entre {valid_types}.")
            return None

        # Verifica se o email já foi cadastrado
        if any(user.email == email for user in db.get_users()):
            print(f"Erro: O email {email} já está em uso.")
            return None

        # Cria um novo usuário (instanciando Client ou Agent)
        if user_type.capitalize() == "Cliente":
            new_user = Client(len(db.get_users()) + 1, name, email, password)
        elif user_type.capitalize() == "Agente":
            new_user = Agent(len(db.get_users()) + 1, name, email, password)

        # Adiciona o novo usuário ao banco de dados
        db.add_user(new_user)
        print(f"Usuário {name} registrado com sucesso como {user_type.capitalize()}!")
        return new_user

    # Lista todos os usuários
    def list_users(self):
        users = db.get_users()
        if not users:
            print("Nenhum usuário cadastrado.")
        for user in users:
            print(user)

    # Deleta um usuário pelo ID
    def delete_user(self, user_id):
        users = db.get_users()
        user_to_delete = next((user for user in users if user.id == user_id), None)
        if user_to_delete:
            db.users.remove(user_to_delete)
            print(f"Usuário {user_to_delete.name} excluído com sucesso.")
            return True
        print(f"Erro: Usuário com ID {user_id} não encontrado.")
        return False

    # Lista apenas os clientes
    def list_clients(self):
        clients = db.get_clients()
        if not clients:
            print("Nenhum cliente cadastrado.")
        for client in clients:
            print(client)

    # Lista apenas os agentes
    def list_agents(self):
        agents = db.get_agents()
        if not agents:
            print("Nenhum agente cadastrado.")
        for agent in agents:
            print(agent)

    def find_user_by_id(self, user_id):
        for user in db.get_users():
            if user.id == user_id:
                return user
        return None