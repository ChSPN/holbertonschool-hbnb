from flask_restx import Namespace, Resource, fields
from entities.amenity import Amenity
from managers.repositoryFileManager import RepositoryFileManager

ns = Namespace("Amenities", description="Amenities operations")

amenity = ns.model(
    "Amenity",
    {
        "id": fields.String(
            readonly=True, description="The amenity unique identifier"
        ),
        "created_at": fields.DateTime(
            readonly=True, description="The amenity created date"
        ),
        "updated_at": fields.DateTime(
            readonly=True, description="The amenity updated date"
        ),
        "name": fields.String(description="The amenity name"),
    },
)


@ns.route("")
class AmenityListResource(Resource):
    def __init__(self, api=None, *args, **kwargs):
        super(AmenityListResource, self).__init__(api, *args, **kwargs)
        self._manager = RepositoryFileManager()

    @ns.doc(description="Get all amenities")
    @ns.marshal_list_with(amenity, code=200)
    def get(self):
        return Amenity.load(self._manager)

    @ns.doc(description="Create a new amenity")
    @ns.expect(amenity)
    @ns.response(201, "Amenity created")
    @ns.response(409, "Amenity already exists")
    @ns.response(400, "Amenity not created")
    def post(self):
        amenity = Amenity(self._manager, self.api.payload)
        if amenity.exist(
            self.api.payload["name"]
            if self.api.payload and "name" in self.api.payload
            else None
        ):
            return "Amenity already exists", 409
        elif amenity.save():
            return "Amenity created", 201
        else:
            return "Amenity not created", 400


@ns.route("/<uuid:id>")
class AmenityResource(Resource):
    def __init__(self, api=None, *args, **kwargs):
        super(AmenityResource, self).__init__(api, *args, **kwargs)
        self._manager = RepositoryFileManager()

    @ns.doc(description="Get amenity by id")
    @ns.marshal_with(amenity, code=200)
    @ns.response(404, "Amenity not found")
    def get(self, id):
        amenity = Amenity.load(self._manager, id)
        if amenity:
            return amenity
        else:
            return "Amenity not found", 404

    @ns.doc(description="Update amenity by id")
    @ns.expect(amenity)
    @ns.response(201, "Amenity updated")
    @ns.response(409, "Amenity already exists")
    @ns.response(404, "Amenity not found")
    @ns.response(400, "Amenity not updated")
    def put(self, id):
        amenity = Amenity.load(self._manager, id)
        if not amenity:
            return "Amenity not found", 404

        amenity.parse(self.api.payload)
        if amenity.exist(
            self.api.payload["name"]
            if self.api.payload and "name" in self.api.payload
            else None
        ):
            return "Amenity already exists", 409
        elif amenity.save():
            return "Amenity updated", 201
        else:
            return "Amenity not updated", 400

    @ns.doc(description="Delete amenity by id")
    @ns.response(204, "Amenity deleted")
    @ns.response(404, "Amenity not found")
    @ns.response(400, "Amenity not deleted")
    def delete(self, id):
        amenity = Amenity.load(self._manager, id)
        if not amenity:
            return "Amenity not found", 404

        if amenity.delete():
            return "Amenity deleted", 204
        else:
            return "Amenity not deleted", 400
