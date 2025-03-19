from app.data.database import db
from app.models.visit import Visit

class VisitController:
    def __init__(self, property_controller, user_controller):
        self.property_controller = property_controller  # Instância de PropertyController
        self.user_controller = user_controller  # Instância de UserController

    def schedule_visit(self, id, client_id, property_id, date_time):
        # Busca a propriedade usando o PropertyController
        property_obj = self.property_controller.find_property_by_id(property_id)
        if not property_obj:
            raise ValueError("Propriedade não encontrada.")

        # Obtém o agente associado à propriedade
        agent = property_obj.agent  # Supondo que a propriedade tenha um atributo 'agent'

        # Busca o cliente usando o UserController
        client = self.user_controller.find_user_by_id(client_id)
        if not client:
            raise ValueError("Cliente não encontrado.")

        # Cria a visita
        new_visit = Visit(id, client, agent, property_obj, date_time)
        db.add_visit(new_visit)
        return new_visit

    def list_visits(self):
        return db.get_visits()  # Retorna todas as visitas do banco de dados

    def find_visit_by_id(self, visit_id):
        for visit in db.get_visits():
            if visit._id == visit_id:
                return visit
        return None

    def cancel_visit(self, visit_id):
        visit_to_cancel = self.find_visit_by_id(visit_id)
        if visit_to_cancel:
            visit_to_cancel.cancel()  # Altera o status para "Cancelado!"
            return True
        return False

    def reschedule_visit(self, visit_id, new_date_time):
        visit_to_reschedule = self.find_visit_by_id(visit_id)
        if visit_to_reschedule:
            visit_to_reschedule.reschedule(new_date_time)  # Reagenda a visita
            return True
        return False