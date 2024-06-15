from flask import Flask
from flask_restx import Api
from resources.userResource import ns as user_ns
from resources.amenityResource import ns as amenity_ns


app = Flask(__name__)
app.config['RESTX_MASK_SWAGGER'] = False
api = Api(app, version='1.0', title='HBNB APIs', description='APIs for HBNB project')

api.add_namespace(user_ns, path='/users')
api.add_namespace(amenity_ns, path='/amenities')

if __name__ == '__main__':
    app.run(debug=True)
