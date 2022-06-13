from flask import Blueprint, request, jsonify
from werkzeug.security import check_password_hash, generate_password_hash, gen_salt
from src.constants.http_status_codes import HTTP_400_BAD_REQUEST, HTTP_409_CONFLICT, HTTP_201_CREATED
import validators
from src.database import User, db



auth = Blueprint("auth", __name__, url_prefix='/api/v1/auth')

@auth.post('/register')
def register():
    email = request.json['email']
    username = request.json['username']
    password = request.json['password']

    if len(password)< 6:
        return jsonify({"error": "Password length must be greater than 6 characters"}), HTTP_400_BAD_REQUEST

    if len(username)< 3:
        return jsonify({"error": "Username length must be greater than 3 characters"}), HTTP_400_BAD_REQUEST

    if not username.isalnum() or " " in username:
        return jsonify({"error": "User should not have spaces and be alphanumeric"}), HTTP_400_BAD_REQUEST

    if not validators.email(email):
        return jsonify({"error": "Please enter a valid email account"}), HTTP_400_BAD_REQUEST

    if User.query.filter_by(email=email).first() is not None:
        return jsonify({"error": "Email is taken"}), HTTP_409_CONFLICT

    if User.query.filter_by(username=username).first() is not None:
        return jsonify({"error": "Username is taken"}), HTTP_409_CONFLICT
    pwd_hash=generate_password_hash(password)

    user = User(email=email, username=username, password=pwd_hash)
    db.session.add(user)
    db.session.commit()

    return jsonify({
        "message": 'User has been successfully created',
        "username": username,
        "email": email
    }), HTTP_201_CREATED
@auth.get('/me')
def me():
    return {"user": "me"}
