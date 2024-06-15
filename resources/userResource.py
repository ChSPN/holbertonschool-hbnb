from flask_restx import Namespace, Resource, fields
from entities.user import User
from managers.repositoryFileManager import RepositoryFileManager

ns = Namespace('Users', description='Users operations')

user = ns.model('User', {
    'created_at': fields.DateTime(readonly=True, description='The user created date'),
    'email': fields.String(description='The user email'),
    'first_name': fields.String(description='The user first name'),
    'id': fields.String(readonly=True, description='The user unique identifier'),
    'last_name': fields.String(description='The user last name'),
    'password': fields.String(description='The user password'),
    'updated_at': fields.DateTime(readonly=True, description='The user updated date')
})

@ns.route('')
class UserListResource(Resource):
    def __init__(self, api=None, *args, **kwargs):
        super(UserListResource, self).__init__(api, *args, **kwargs)
        self._manager = RepositoryFileManager()

    @ns.doc(description='Get all users')
    @ns.marshal_list_with(user, code=200)
    def get(self):
        return User.load(self._manager)

    @ns.doc(description='Create a new user')
    @ns.expect(user, validate=True)
    @ns.response(201, 'User created')
    @ns.response(409, 'Invalid email')
    @ns.response(400, 'User not created')
    def post(self):
        user = User(self._manager, self.api.payload)
        if not user.validate_email():
            return 'Invalid email', 409
        elif user.save():
            return 'User created', 201
        else:
            return 'User not created', 400

@ns.route('/<uuid:id>')
class UserResource(Resource):
    def __init__(self, api=None, *args, **kwargs):
        super(UserResource, self).__init__(api, *args, **kwargs)
        self._manager = RepositoryFileManager()

    @ns.doc(description='Get user by id')
    @ns.marshal_with(user, code=200)
    @ns.response(404, 'User not found')
    def get(self, id):
        user = User.load(self._manager, id)
        if user:
            return user
        else:
            return 'User not found', 404

    @ns.doc(description='Update user by id')
    @ns.expect(user, validate=True)
    @ns.response(201, 'User updated')
    @ns.response(409, 'Invalid email')
    @ns.response(404, 'User not found')
    @ns.response(400, 'User not updated')
    def put(self, id):
        user = User.load(self._manager, id)
        if not user:
            return 'User not found', 404

        user.email = self.api.payload['email']
        user.first_name = self.api.payload['first_name']
        user.last_name = self.api.payload['last_name']
        user.password = self.api.payload['password']
        if not user.validate_email():
            return 'Invalid email', 409
        elif user.save():
            return 'User updated', 201
        else:
            return 'User not updated', 400

    @ns.doc(description='Delete user by id')
    @ns.response(204, 'User deleted')
    @ns.response(404, 'User not found')
    @ns.response(400, 'User not deleted')
    def delete(self, id):
        user = User.load(self._manager, id)
        if not user:
            return 'User not found', 404

        if user.delete():
            return 'User deleted', 204
        else:
            return 'User not deleted', 400
