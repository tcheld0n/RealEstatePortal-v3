from app.data.database import db
from app.models.review import Review

class ReviewController:
    def add_review(self, id, reviewer_id, property_id, rating, comment):
        reviewer = self.find_reviewer_by_id(reviewer_id)
        if reviewer:
            new_review = Review(id, reviewer, property_id, rating, comment)
            db.add_review(new_review)
            return new_review
        return None

    def list_reviews(self):
        return [vars(review) for review in db.reviews]

    def delete_review(self, review_id):
        review_to_delete = self.find_review_by_id(review_id)
        if review_to_delete:
            db.reviews.remove(review_to_delete)
            return True
        return False