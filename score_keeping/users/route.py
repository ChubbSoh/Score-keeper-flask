from flask import Flask, jsonify, Blueprint, request, render_template
from score_keeping.users.models import User
from score_keeping import db, app
from sqlalchemy.exc import IntegrityError
from score_keeping.helpers.auth import generate_token, requires_auth, verify_token


users_api_blueprint = Blueprint('users_api',
                             __name__,
                             template_folder='templates')



@users_api_blueprint.route('/signup', methods = ['POST'])
def create_user():
    
    post_data = request.get_json()
    
    try:
        user = User(
            name=post_data['user']["name"],
            email=post_data['user']["email"], 
            password=post_data['user']["password"]
        )

        db.session.add(user)
        db.session.commit()

# the problem with this is that the user doesnt know what they did wrong.
# FIX!!!
    except IntegrityError:
        return jsonify(message="User with that email already exists"), 409

    new_user = User.query.filter_by(email=post_data['user']["email"]).first()

    return jsonify(
        id=user.id,
        token=generate_token(new_user)
        )

@users_api_blueprint.route('/login', methods = ['GET'])
def login():
    post_data = request.get_json()
    user = User.get_with_email_and_password(post_data['user']["email"], post_data["password"])
    if user:
        return jsonify(token=generate_token(user))
    else:
        return jsonify(error=True), 403





