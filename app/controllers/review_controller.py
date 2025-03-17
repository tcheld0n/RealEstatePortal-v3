from app.data.database import db
from app.models.review import Review
from app.controllers.property_controller import PropertyController

class ReviewController:
    def add_review(self, id, reviewer_id, property_id, rating, comment):
        # Validação da nota
        if rating < 1 or rating > 5:
            raise ValueError("A nota deve estar entre 1 e 5.")

        # Verifica se a propriedade existe (usando PropertyController)
        property_controller = PropertyController()
        if not property_controller.find_property_by_id(property_id):
            raise ValueError("Propriedade não encontrada.")

        # Cria e adiciona a avaliação
        new_review = Review(id, reviewer_id, property_id, rating, comment)
        db.add_review(new_review)
        return new_review

    def list_reviews(self):
        return [vars(review) for review in db.reviews]

    def find_review_by_id(self, review_id):
        for review in db.reviews:
            if review.id == review_id:
                return review
        return None

    def delete_review(self, review_id):
        review_to_delete = self.find_review_by_id(review_id)
        if review_to_delete:
            db.reviews.remove(review_to_delete)
            return True
        return False

    def get_reviews_by_property(self, property_id):
        return [review for review in db.reviews if review.property_id == property_id]

    def get_average_rating(self, property_id):
        reviews = self.get_reviews_by_property(property_id)
        if not reviews:
            return 0
        total = sum(review.rating for review in reviews)
        return total / len(reviews)