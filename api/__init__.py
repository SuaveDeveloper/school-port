


from flask import Flask
# from flask import app
from flask_restx import Api

from api.models.students import Student
from .resources.views import portal_namespace
from .auth.views import auth_namespace
from .config.config import config_dict
from .utils import db
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from werkzeug.exceptions import NotFound,MethodNotAllowed
from flask_sqlalchemy import SQLAlchemy



def create_app(config=config_dict['dev']):
    app = Flask(__name__)

    app.config.from_object(config)

    # app.config.from_mapping(
    #     DATABASE_URI="postgres://postgres:piperlead@127.0.0.1:5432/student_db"
    # )

    # db.init_app(app)

    # app.config.from_object(config)
    db = SQLAlchemy(app=app).init_app(app)
    # print(db)
    # db.init.app()

    jwt = JWTManager(app)

    migrate = Migrate(app, db)

    authorizations = {
        "Bearer Auth": {
            "type": "apiKey",
            "in": "header",
            "name": "Authorization",
            "description": "Add a JWT token to the header with ** Bearer &lt;JWT&gt; ** token to authorize"
        }
    }



    api = Api(app)

    api.add_namespace(portal_namespace)
    api.add_namespace(auth_namespace, path='/auth')

    @api.errorhandler(NotFound)
    def not_found(error):
        return {"error": "Not Found"}, 404

    @api.errorhandler(MethodNotAllowed)
    def method_not_allowed(error):
        return {"error": "Method Not Allowed"}, 404

    @app.shell_context_processor
    def make_shell_context():
        return{
            'db': db,
            'Student': Student,
        }

    return app



