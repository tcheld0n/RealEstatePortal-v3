from app.data.database import db
from app.models.visit import Visit
from app.models.client import Client
from app.models.agent import Agent

class VisitController:
    def __init__(self, property_controller, user_controller):
        self.property_controller = property_controller  # Instância de PropertyController
        self.user_controller = user_controller  # Instância de UserController

    def schedule_visit(self, id, client_id, agent_id, property_id, date_time):
        # Busca o cliente usando o UserController
        client = self.user_controller.find_user_by_id(client_id)
        # if not client or not isinstance("cliente", Client):  # Verifica se é um cliente
        #     raise ValueError("Cliente não encontrado.")
        # if client.get_role() != "client":
        #     raise ValueError("Cliente não encontrado.")
        #
        # # Busca o agente usando o UserController
        # agent = self.user_controller.find_user_by_id(agent_id)
        # # if not agent or not isinstance(agent, Agent):  # Verifica se é um agente
        # #     raise ValueError("Agente não encontrado.")
        # if agent.get_role() != "agent":
        #     raise ValueError("Agente não encontrado.")

        # Busca a propriedade usando o PropertyController
        property_obj = self.property_controller.find_property_by_id(property_id)
        if not property_obj:
            raise ValueError("Propriedade não encontrada.")

        # Cria a visita
        new_visit = Visit(id, client, agent, property_obj, date_time)
        db.add_visit(new_visit)
        return new_visit

    def list_visits(self):
        return [vars(visit) for visit in db.visits]

    def find_visit_by_id(self, visit_id):
        for visit in db.visits:
            if visit.id == visit_id:
                return visit
        return None

    def cancel_visit(self, visit_id):
        visit_to_cancel = self.find_visit_by_id(visit_id)
        if visit_to_cancel:
            db.visits.remove(visit_to_cancel)
            return True
        return False