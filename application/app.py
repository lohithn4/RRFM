from flask import request, render_template, jsonify, url_for, redirect, g
from .models import User
from index import app, db
from .utils.auth import generate_token, requires_auth, verify_token


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/<path:path>', methods=['GET'])
def any_root_path(path):
    return render_template('index.html')


@app.route("/api/user", methods=["GET"])
@requires_auth
def get_user():
    return jsonify(result=g.current_user)


@app.route("/api/create_user", methods=["POST"])
def create_user():
    try:
        incoming = request.get_json()
        email = incoming['email']
        password = incoming['password']
    except:
        return jsonify()
    if not email or not password:
        return jsonify(message="User with that email already exists"), 409
    u = User(email=email, password=password)
    try:
        u.save()
        print "came_here______"
    except db.NotUniqueError:
        print "came_here______Email already exists"
        return jsonify(message="Email already exists"), 409
    except db.ValidationError:
        print "came_here______Email format incorrect "
        return jsonify(message="Email format incorrect "), 409
    new_user = User.objects.get(email=email)
    print "___new_user___%s" % new_user
    return jsonify(
        token=generate_token(new_user)
    )


@app.route("/api/get_token", methods=["POST"])
def get_token():
    incoming = request.get_json()
    user = User.get_user_with_email_and_password(incoming["email"], incoming["password"])
    if user:
        print "__________last______user=%s" % user
        return jsonify(token=generate_token(user))

    return jsonify(error=True), 403


@app.route("/api/is_token_valid", methods=["POST"])
def is_token_valid():
    incoming = request.get_json()
    is_valid = verify_token(incoming["token"])

    if is_valid:
        return jsonify(token_is_valid=True)
    else:
        return jsonify(token_is_valid=False), 403
