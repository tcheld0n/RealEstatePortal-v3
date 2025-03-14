from app.models.user import User

class Client(User):
    def __init__(self, user_id, name, email, password):
        super().__init__(user_id, name, email, password)
        self._scheduled_visits = []

    def schedule_visit(self, visit):
        self._scheduled_visits.append(visit)

    def list_scheduled_visits(self):
        return self._scheduled_visits

    def get_role(self):
        return "Cliente"
