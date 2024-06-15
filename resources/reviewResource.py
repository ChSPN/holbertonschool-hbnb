from flask_restx import Namespace, Resource, fields
from entities.place import Place
from entities.review import Review
from managers.repositoryFileManager import RepositoryFileManager

ns = Namespace('Reviews', description='Reviews operations')

review = ns.model('Review', {
    'id': fields.String(readonly=True, description='The review unique identifier'),
    'created_at': fields.DateTime(readonly=True, description='The review created date'),
    'updated_at': fields.DateTime(readonly=True, description='The review updated date'),
    'place_id': fields.String(readonly=True, description='The review place id'),
    'comment': fields.String(description='The review comment'),
    'rating': fields.Integer(description='The review rating'),
    'user_id': fields.String(description='The review user id'),
})

'''POST /places/{place_id}/reviews: Create a new review for a specified place.
GET /places/{place_id}/reviews: Retrieve all reviews for a specific place.
GET /users/{user_id}/reviews: Retrieve all reviews written by a specific user.'''

@ns.route('places/<uuid:place_id>/reviews')
class ReviewPlaceResource(Resource):
    def __init__(self, api=None, *args, **kwargs):
        super(ReviewPlaceResource, self).__init__(api, *args, **kwargs)
        self._manager = RepositoryFileManager()

    @ns.doc(description='Get all reviews of the place')
    @ns.marshal_list_with(review, code=200)
    @ns.response(404, 'Reviews not found')
    def get(self, place_id):
        reviews = Review.load_by_place(self._manager, place_id)
        if not reviews:
            return 'Reviews not found', 404
        else:
            return reviews

    @ns.doc(description='Create a new review for the place')
    @ns.expect(review)
    @ns.response(201, 'Review created')
    @ns.response(404, 'Place not exist')
    @ns.response(400, 'Review not created')
    def post(self, place_id):
        review = Review(self._manager, self.api.payload)
        review.place_id = place_id
        if not review.exist_place():
            return 'Place not exist', 404

        if review.save():
            return 'Review created', 201
        else:
            return 'Review not created', 400

@ns.route('users/<uuid:user_id>/reviews')
class ReviewUserResource(Resource):
    def __init__(self, api=None, *args, **kwargs):
        super(ReviewUserResource, self).__init__(api, *args, **kwargs)
        self._manager = RepositoryFileManager()

    @ns.doc(description='Get all reviews of the user')
    @ns.marshal_list_with(review, code=200)
    @ns.response(404, 'Reviews not found')
    def get(self, user_id):
        reviews = Review.load_by_user(self._manager, user_id)
        if not reviews:
            return 'Reviews not found', 404
        else:
            return reviews

@ns.route('reviews/<uuid:id>')
class ReviewResource(Resource):
    def __init__(self, api=None, *args, **kwargs):
        super(ReviewResource, self).__init__(api, *args, **kwargs)
        self._manager = RepositoryFileManager()

    @ns.doc(description='Get review by id')
    @ns.marshal_with(review, code=200)
    @ns.response(404, 'Review not found')
    def get(self, id):
        review = Review.load(self._manager, id)
        if review:
            return review
        else:
            return 'Review not found', 404

    @ns.doc(description='Update review by id')
    @ns.expect(review)
    @ns.response(201, 'Review updated')
    @ns.response(404, 'Review not found')
    @ns.response(400, 'Review not updated')
    def put(self, id):
        review = Review.load(self._manager, id)
        if not review:
            return 'Review not found', 404

        review.parse(self.api.payload)
        if review.save():
            return 'Review updated', 201
        else:
            return 'Review not updated', 400

    @ns.doc(description='Delete review by id')
    @ns.response(204, 'Review deleted')
    @ns.response(404, 'Review not found')
    @ns.response(400, 'Review not deleted')
    def delete(self, id):
        review = Review.load(self._manager, id)
        if not review:
            return 'Review not found', 404

        if review.delete():
            return 'Review deleted', 204
        else:
            return 'Review not deleted', 400
