from flask import Blueprint, request, jsonify
from models import db, User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token

auth = Blueprint("auth", __name__)

@auth.route("/register", methods=["POST"])
def register():
    data = request.json

    hashed_password = generate_password_hash(data["password"])

    user = User(
        name=data["name"],
        email=data["email"],
        password=hashed_password
    )

    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "User registered successfully"})


@auth.route("/login", methods=["POST"])
def login():
    data = request.json
    user = User.query.filter_by(email=data["email"]).first()

    if user and check_password_hash(user.password, data["password"]):
        token = create_access_token(identity=str(user.id))
        return jsonify({"access_token": token})

    return jsonify({"error": "Invalid credentials"}), 401
