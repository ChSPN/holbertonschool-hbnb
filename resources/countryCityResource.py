from flask_restx import Namespace, Resource, fields
from entities.city import City
from entities.country import Country
from managers.repositoryFileManager import RepositoryFileManager

ns = Namespace('Countries and Cities', description='Countries and Cities operations')

country = ns.model('Country', {
    'id': fields.String(readonly=True, description='The country unique identifier'),
    'created_at': fields.DateTime(readonly=True, description='The country created date'),
    'updated_at': fields.DateTime(readonly=True, description='The country updated date'),
    'name': fields.String(description='The country name'),
    'code': fields.String(description='The country code')
})

city = ns.model('City', {
    'id': fields.String(readonly=True, description='The city unique identifier'),
    'created_at': fields.DateTime(readonly=True, description='The city created date'),
    'updated_at': fields.DateTime(readonly=True, description='The city updated date'),
    'name': fields.String(description='The city name'),
    'country_id': fields.String(description='The country id')
})

@ns.route('countries')
class CountryListResource(Resource):
    def __init__(self, api=None, *args, **kwargs):
        super(CountryListResource, self).__init__(api, *args, **kwargs)
        self._manager = RepositoryFileManager()

    @ns.doc(description='Get all countries')
    @ns.marshal_list_with(country, code=200)
    def get(self):
        return Country.load(self._manager)

    @ns.doc(description='Create a new country')
    @ns.expect(country)
    @ns.response(201, 'Country created')
    @ns.response(409, 'Country already exists')
    @ns.response(400, 'Country not created')
    def post(self):
        country = Country(self._manager, self.api.payload)
        if (country.exist(self.api.payload['name'] if self.api.payload and 'name' in self.api.payload else None) 
            or country.exist(self.api.payload['code'] if self.api.payload and 'code' in self.api.payload else None)):
            return 'Country already exists', 409
        elif country.save():
            return 'Country created', 201
        else:
            return 'Country not created', 400

@ns.route('countries/<string:country_code>')
class CountryResource(Resource):
    def __init__(self, api=None, *args, **kwargs):
        super(CountryResource, self).__init__(api, *args, **kwargs)
        self._manager = RepositoryFileManager()

    @ns.doc(description='Get country by code')
    @ns.marshal_with(country, code=200)
    @ns.response(404, 'Country not found')
    def get(self, country_code):
        country = Country.load_by_code(self._manager, country_code)
        if country:
            return country
        else:
            return 'Country not found', 404

@ns.route('countries/<string:country_code>/cities')
class CountryCityResource(Resource):
    def __init__(self, api=None, *args, **kwargs):
        super(CountryCityResource, self).__init__(api, *args, **kwargs)
        self._manager = RepositoryFileManager()

    @ns.doc(description='Get cities by country code')
    @ns.marshal_list_with(city, code=200)
    @ns.response(404, 'Cities not found')
    def get(self, country_code):
        cities = City.load_by_country_code(self._manager, country_code)
        if cities:
            return cities
        else:
            return 'Cities not found', 404

@ns.route('cities')
class CityListResource(Resource):
    def __init__(self, api=None, *args, **kwargs):
        super(CityListResource, self).__init__(api, *args, **kwargs)
        self._manager = RepositoryFileManager()

    @ns.doc(description='Get all cities')
    @ns.marshal_list_with(city, code=200)
    def get(self):
        return City.load(self._manager)

    @ns.doc(description='Create a new city')
    @ns.expect(city)
    @ns.response(201, 'City created')
    @ns.response(409, 'City already exists')
    @ns.response(400, 'City not created')
    def post(self):
        city = City(self._manager, self.api.payload)
        if city.exist():
            return 'City already exists', 409
        elif city.save():
            return 'City created', 201
        else:
            return 'City not created', 400

@ns.route('cities/<uuid:id>')
class CityResource(Resource):
    def __init__(self, api=None, *args, **kwargs):
        super(CityResource, self).__init__(api, *args, **kwargs)
        self._manager = RepositoryFileManager()

    @ns.doc(description='Get city by id')
    @ns.marshal_with(city, code=200)
    @ns.response(404, 'City not found')
    def get(self, id):
        city = City.load(self._manager, id)
        if city:
            return city
        else:
            return 'City not found', 404

    @ns.doc(description='Update city by id')
    @ns.expect(city)
    @ns.response(201, 'City updated')
    @ns.response(409, 'City already exists')
    @ns.response(404, 'City not found')
    @ns.response(400, 'City not updated')
    def put(self, id):
        city = City.load(self._manager, id)
        if not city:
            return 'City not found', 404

        city.parse(self.api.payload)
        if city.exist(self.api.payload['name'] if self.api.payload and 'name' in self.api.payload else None):
            return 'City already exists', 409
        elif city.save():
            return 'City updated', 201
        else:
            return 'City not updated', 400

    @ns.doc(description='Delete city by id')
    @ns.response(204, 'City deleted')
    @ns.response(404, 'City not found')
    @ns.response(400, 'City not deleted')
    def delete(self, id):
        city = City.load(self._manager, id)
        if not city:
            return 'City not found', 404

        if city.delete():
            return 'City deleted', 204
        else:
            return 'City not deleted', 400
