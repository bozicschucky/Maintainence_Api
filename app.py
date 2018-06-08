from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, Requests

app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'code'
api = Api(app)

jwt = JWT(app, authenticate, identity)

# api.add_resource(Item, '/request/<int:id>')
api.add_resource(Requests, '/app/v2/requests')
api.add_resource(UserRegister, '/app/v2/auth/signup')

if __name__ == '__main__':
    app.run(debug=True)  # important to mention debug=True
