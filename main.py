# from API import create_app
# # from api.config.config import config_dict

# # app = create_app()
# from flask import Flask
# from flask_restx import Api

# app = Flask(__name__)
# api = Api(app)


# if __name__ == "__main__":
#     app.run(debug=True)


# from flask import Flask

# def create__app():
#     app= Flask(__name__)

#     return app


from api import create_app
from api.config.config import config_dict

app = create_app(config=config_dict['dev'])
# app = create_app()


if __name__ == "__main__":
    app.run(debug=True)