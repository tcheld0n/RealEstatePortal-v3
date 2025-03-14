from datetime import datetime

class Review:
    def __init__(self, id, property, user, rating, comment):
        self._id = id
        self._property = property
        self._user = user
        self._rating = rating
        self._comment = comment
        self._date = datetime.now()

    # Getters e setters para rating
    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, value):
        if not (1 <= value <= 5):
            raise ValueError("A avaliação deve estar entre 1 e 5.")
        self._rating = value

    # Getters e setters para comment
    @property
    def comment(self):
        return self._comment

    @comment.setter
    def comment(self, value):
        if not value:
            raise ValueError("O comentário não pode ser vazio.")
        self._comment = value

    # Getter para date (somente leitura)
    @property
    def date(self):
        return self._date

    # Método para atualizar a avaliação
    def update_review(self, rating=None, comment=None):
        if rating:
            self.rating = rating  # Usa o setter
        if comment:
            self.comment = comment  # Usa o setter