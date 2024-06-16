from flask import Flask
from flask_restx import Api
from resources.userResource import ns as user_ns
from resources.countryCityResource import ns as country_city_ns
from resources.amenityResource import ns as amenity_ns
from resources.placeResource import ns as place_ns
from resources.reviewResource import ns as review_ns


app = Flask(__name__)
app.config['RESTX_MASK_SWAGGER'] = False
api = Api(app, version='1.0', title='HBNB APIs', description='APIs for HBNB project')

api.add_namespace(user_ns, path='/users')
api.add_namespace(country_city_ns, path='/')
api.add_namespace(amenity_ns, path='/amenities')
api.add_namespace(place_ns, path='/places')
api.add_namespace(review_ns, path='/')

if __name__ == '__main__':
    app.run(debug=True)
