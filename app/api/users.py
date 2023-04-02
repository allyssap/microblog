from flask import jsonify, request, url_for, abort, current_app
from app import db
from app.models import User, Post
from app.api import bp
from app.api.auth import token_auth
from app.api.errors import bad_request


@bp.route('/users/<int:id>', methods=['GET'])
@token_auth.login_required
def get_user(id):
    return jsonify(User.query.get_or_404(id).to_dict())


@bp.route('/users', methods=['GET'])
@token_auth.login_required
def get_users():
    page = request.args.get('page', 1, type=int)
    per_page = min(request.args.get('per_page', 10, type=int), 100)
    data = User.to_collection_dict(User.query, page, per_page, 'api.get_users')
    return jsonify(data)


@bp.route('/users/<int:id>/followers', methods=['GET'])
@token_auth.login_required
def get_followers(id):
    user = User.query.get_or_404(id)
    page = request.args.get('page', 1, type=int)
    per_page = min(request.args.get('per_page', 10, type=int), 100)
    data = User.to_collection_dict(user.followers, page, per_page,
                                   'api.get_followers', id=id)
    return jsonify(data)


@bp.route('/users/<int:id>/followed', methods=['GET'])
@token_auth.login_required
def get_followed(id):
    user = User.query.get_or_404(id)
    page = request.args.get('page', 1, type=int)
    per_page = min(request.args.get('per_page', 10, type=int), 100)
    data = User.to_collection_dict(user.followed, page, per_page,
                                   'api.get_followed', id=id)
    return jsonify(data)


@bp.route('/users', methods=['POST'])
def create_user():
    data = request.get_json() or {}
    if 'username' not in data or 'email' not in data or 'password' not in data:
        return bad_request('must include username, email and password fields')
    if User.query.filter_by(username=data['username']).first():
        return bad_request('please use a different username')
    if User.query.filter_by(email=data['email']).first():
        return bad_request('please use a different email address')
    user = User()
    user.from_dict(data, new_user=True)
    db.session.add(user)
    db.session.commit()
    response = jsonify(user.to_dict())
    response.status_code = 201
    response.headers['Location'] = url_for('api.get_user', id=user.id)
    return response

@bp.route('/user/<username>', methods=['GET'])
@token_auth.login_required
def get_profile(username):
    user = User.query.filter_by(username=username).first_or_404()
    page = request.args.get('page', 1, type=int)
    posts = user.posts.order_by(Post.timestamp.desc()).paginate(
        page=page, per_page=current_app.config['POSTS_PER_PAGE'],
        error_out=False)
    next_url = url_for('api.get_user', username=user.username,
                       page=posts.next_num) if posts.has_next else None
    prev_url = url_for('api.get_user', username=user.username,
                       page=posts.prev_num) if posts.has_prev else None
    posts_data = []
    for post in posts.items:
        post_data = {
            'id': post.id,
            'body': post.body,
            'timestamp': post.timestamp
        }
        posts_data.append(post_data)
    user_data = {
        'id': user.id,
        'username': user.username,
        'posts': posts_data,
        'next_url': next_url,
        'prev_url': prev_url
    }
    response = jsonify(user_data)
    response.status_code = 201
    return response

@bp.route('/users/<int:id>', methods=['PUT'])
@token_auth.login_required
def update_user(id):
    if token_auth.current_user().id != id:
        abort(403)
    user = User.query.get_or_404(id)
    data = request.get_json() or {}
    if 'username' in data and data['username'] != user.username and \
            User.query.filter_by(username=data['username']).first():
        return bad_request('please use a different username')
    if 'email' in data and data['email'] != user.email and \
            User.query.filter_by(email=data['email']).first():
        return bad_request('please use a different email address')
    user.from_dict(data, new_user=False)
    db.session.commit()
    return jsonify(user.to_dict())

@bp.route('/home', methods=['GET'])
def home_page():
    # return json of URLs for registering, reseting password, and answering security question
    paths = {
        'register' : url_for('auth.register'),
        'reset password' : url_for('auth.reset_password_request'),
        'security question' : url_for('auth.get_user')
    }
    response = jsonify(paths)
    response.status_code = 200
    return response

@bp.route('/otp', methods=['POST'])
def otp():
    # verify otp matches otp for certain user
    req_data = request.get_json()
    username = req_data['username']
    otp = req_data['otp']

    user = User.query.filter_by(username=username).first()
    if user is None:
        return jsonify({'error': 'Invalid username or password'}), 401

    if otp != '1234':
        return jsonify({'error': 'Invalid OTP'}), 401

    response = jsonify({'message': 'Logged in successfully'})
    response.status_code = 201
    return response

@bp.route('/', methods=['GET'])
@bp.route('/index', methods=['GET'])
@token_auth.login_required
def index():
    # retrieve index page data json, specifically URL for profile page
    req_data = request.get_json()
    username = req_data['username']
    user = User.query.filter_by(username=username).first_or_404()
    if user is None:
        return jsonify({'error': 'user account not in table'}), 401
    page = request.args.get('page', 1, type=int)
    posts = user.followed_posts().paginate(
        page=page, per_page=current_app.config['POSTS_PER_PAGE'],
        error_out=False)

    posts_list = []
    for post in posts.items:
        posts_list.append({
            'id': post.id,
            'body': post.body,
            'author': {
                'id': post.author.id,
                'username': post.author.username
            },
            'product': post.product,
            'company': post.company,
            'category': post.category,
            'timestamp': post.timestamp
        })

    data = {
        'posts': posts_list,
        'has_next': posts.has_next,
        'next_page': posts.next_num,
        'has_prev': posts.has_prev,
        'prev_page': posts.prev_num,
        'total_pages': posts.pages,
        'profile link' : url_for('main.user', username=user.username)
    }
    response = jsonify(data)
    response.status_code = 200
    return response
