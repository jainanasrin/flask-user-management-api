from flask import Flask
from flask_jwt_extended import JWTManager
from models import db
from auth import auth
from routes import routes
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
jwt = JWTManager(app)

app.register_blueprint(auth)
app.register_blueprint(routes)

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
