from app.data.database import db
from app.models.visit import Visit

class VisitController:
    def __init__(self, property_controller):
        self.property_controller = property_controller  # Instanciando PropertyController

    def schedule_visit(self, id, client_id, agent_id, property_id, date_time):
        client = self.find_client_by_id(client_id)
        agent = self.find_agent_by_id(agent_id)
        property_obj = self.property_controller.find_property_by_id(property_id)  # Usando o método de PropertyController

        if client and agent and property_obj:
            new_visit = Visit(id, client, agent, property_obj, date_time)
            db.add_visit(new_visit)
            return new_visit
        return None

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