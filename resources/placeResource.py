from flask_restx import Namespace, Resource, fields
from entities.amenity import Amenity
from entities.place import Place
from managers.repositoryFileManager import RepositoryFileManager

ns = Namespace('Places', description='Places operations')

place = ns.model('Place', {
    'id': fields.String(readonly=True, description='The place unique identifier'),
    'created_at': fields.DateTime(readonly=True, description='The place created date'),
    'updated_at': fields.DateTime(readonly=True, description='The place updated date'),
    'city_id': fields.String(description='The place city identifier'),
    'description': fields.String(description='The place description'),
    'host_id': fields.String(description='The place host identifier'),
    'name': fields.String(description='The place name'),
    'address': fields.String(description='The place address'),
    'number_of_rooms': fields.Integer(description='The place number of rooms'),
    'number_of_bathrooms': fields.Integer(description='The place number of bathrooms'),
    'price_per_night': fields.Float(description='The place price per night'),
    'max_guests': fields.Integer(description='The place max guests'),
    'latitude': fields.Float(description='The place latitude'),
    'longitude': fields.Float(description='The place longitude'),
    'amenity_ids': fields.List(fields.String(description='The place amenity identifier'), description='The place amenity identifiers'),
})

@ns.route('')
class PlaceListResource(Resource):
    def __init__(self, api=None, *args, **kwargs):
        super(PlaceListResource, self).__init__(api, *args, **kwargs)
        self._manager = RepositoryFileManager()

    @ns.doc(description='Get all places')
    @ns.marshal_list_with(place, code=200)
    def get(self):
        return Place.load(self._manager)

    @ns.doc(description='Create a new place')
    @ns.expect(place)
    @ns.response(201, 'Place created')
    @ns.response(400, 'Place not created')
    def post(self):
        place = Place(self._manager, self.api.payload)
        if place.save():
            return 'Place created', 201
        else:
            return 'Place not created', 400

@ns.route('/<uuid:id>')
class PlaceResource(Resource):
    def __init__(self, api=None, *args, **kwargs):
        super(PlaceResource, self).__init__(api, *args, **kwargs)
        self._manager = RepositoryFileManager()

    @ns.doc(description='Get place by id')
    @ns.marshal_with(place, code=200)
    @ns.response(404, 'Place not found')
    def get(self, id):
        place = Place.load(self._manager, id)
        if place:
            return place
        else:
            return 'Place not found', 404

    @ns.doc(description='Update place by id')
    @ns.expect(place)
    @ns.response(201, 'Place updated')
    @ns.response(404, 'Place not found')
    @ns.response(400, 'Place not updated')
    def put(self, id):
        place = Place.load(self._manager, id)
        if not place:
            return 'Place not found', 404

        place.parse(self.api.payload)
        if place.save():
            return 'Place updated', 201
        else:
            return 'Place not updated', 400

    @ns.doc(description='Delete place by id')
    @ns.response(204, 'Place deleted')
    @ns.response(404, 'Place not found')
    @ns.response(400, 'Place not deleted')
    def delete(self, id):
        place = Place.load(self._manager, id)
        if not place:
            return 'Place not found', 404

        if place.delete():
            return 'Place deleted', 204
        else:
            return 'Place not deleted', 400
