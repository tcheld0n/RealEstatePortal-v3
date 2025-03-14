class Inquiry:
    def __init__(self, id, client, property, message):
        self._id = id
        self._client = client
        self._property = property
        self._message = message
        self._status = "Pendente"

    def update_status(self, status):
        self._status = status

    def __str__(self):
        return f"Consulta #{self._id} - {self._property.title} | Status: {self._status}"

class InquiryController:
    def __init__(self):
        self._inquiries = []

    def add_inquiry(self, client, property, message):
        new_inquiry = Inquiry(len(self._inquiries) + 1, client, property, message)
        self._inquiries.append(new_inquiry)
        return new_inquiry

    def list_inquiries(self):
        return [inquiry for inquiry in self._inquiries]