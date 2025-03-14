from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, user_id, name, email, password):
        self._id = user_id
        self._name = name
        self._email = email
        self._password = password

    # Getters e setters
    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("O nome não pode ser vazio.")
        self._name = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if not value:
            raise ValueError("O email não pode ser vazio.")
        self._email = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        if not value:
            raise ValueError("A senha não pode ser vazia.")
        self._password = value

    @abstractmethod
    def get_role(self):
        pass

    def __str__(self):
        return f"Usuário: {self._name} ({self._email})"