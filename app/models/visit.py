class Visit:
    def __init__(self, id, client, agent, property, date_time):
        if not all([client, agent, property, date_time]):
            raise ValueError("Todos os campos (cliente, agente, propriedade, data/hora) são obrigatórios.")
        self._id = id
        self._client = client
        self._agent = agent
        self._property = property
        self._date_time = date_time
        self._status = "Agendado!"

    def __str__(self):
        return f"Visita #{self._id} - {self._property.title} | Data: {self._date_time} | Status: {self._status}"

    # Getters e setters para date_time
    @property
    def date_time(self):
        return self._date_time

    @date_time.setter
    def date_time(self, value):
        if not value:
            raise ValueError("A data e hora não podem ser vazias.")
        self._date_time = value

    # Getter para status (somente leitura)
    @property
    def status(self):
        return self._status

    # Método para reagendar a visita
    def reschedule(self, new_date_time):
        self.date_time = new_date_time  # Usa o setter
        self._status = "Reagendado!"

    # Método para cancelar a visita
    def cancel(self):
        self._status = "Cancelado!"