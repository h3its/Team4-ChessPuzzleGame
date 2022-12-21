from flask import abort, jsonify, request, session
from sqlalchemy.exc import IntegrityError
from . import app, auth, db, password_hasher
from chess.models import User, Score

@app.route("/health", methods=['GET'])
def health():
    return 'ok'

@auth.verify_password
def verify_password(email, password):
    print('VERIFY PASSWORD')
    print(email, password)
    user = db.session.query(User).where(User.email == email).one_or_none()
    if user and password_hasher.verify(password, user.password):
        return user
    else:
        return False

@app.before_request
def before_request():
    if "health" not in request.endpoint:
        print(request.method, request.endpoint, request.authorization)


@app.route("/users", methods=['POST'])
def create_user():
    email = request.json.get('email')
    password = request.json.get('password')
    user = User(email=email, password=password_hasher.hash(password))
    try:
        db.session.add(user)
        db.session.commit()
    except IntegrityError:
        print('User already exists...')
    
    return jsonify(user)

@app.route("/user", methods=['GET'])
@auth.login_required
def get_user():
    user = auth.current_user()
    user.password = None
    return jsonify(user)

@app.route("/scores", methods=['POST'])
@auth.login_required
def save_scores():
    score = request.json.get('score')
    level = request.json.get('level')
    user = auth.current_user()
    score_entry = Score(user.email, score, level)
    db.session.add(score_entry)
    db.session.commit()
    
    return jsonify(score_entry)

@app.route("/scores/top", methods=['GET'])
@auth.login_required
def get_high_score():
    user = auth.current_user()
    score = db.session.query(Score).where(Score.user_email == user.email).order_by(Score.score.asc()).limit(1).one_or_none()

    return jsonify(score)

@app.route("/users/leaders", methods=['GET'])
def get_leaders():
    level = request.args.get('level')
    if not level:
        return abort(400)
    else:
        leaders = db.session.query(Score).where(Score.level == level).order_by(Score.score.asc()).limit(3).all()
    
        return jsonify(leaders)

