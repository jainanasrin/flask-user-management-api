from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import User, db

routes = Blueprint("routes", __name__)

@routes.route("/profile", methods=["GET"])
@jwt_required()
def profile():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)

    return jsonify({
        "id": user.id,
        "name": user.name,
        "email": user.email
    })


@routes.route("/update", methods=["PUT"])
@jwt_required()
def update_user():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)

    data = request.json
    user.name = data.get("name", user.name)
    user.email = data.get("email", user.email)

    db.session.commit()

    return jsonify({"message": "Updated successfully"})


@routes.route("/delete", methods=["DELETE"])
@jwt_required()
def delete_user():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)

    db.session.delete(user)
    db.session.commit()

    return jsonify({"message": "User deleted"})
