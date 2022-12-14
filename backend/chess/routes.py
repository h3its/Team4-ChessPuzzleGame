from flask import abort, request, session

def configure_routes(app, auth, users, scores):

    @auth.verify_password
    def verify_password(email, password):
        user = users[email]
        if user and password == user['password']:
            return user
        else:
            return False

    @app.before_request
    def before_request():
        print("REQUEST...")
        print(request.method, request.endpoint, request.authorization)

    @app.route("/users", methods=['POST'])
    def create_user():
        email = request.json.get('email')
        password = request.json.get('password')
        user = { 'email': email, 'password': password }
        users[email] = user
        return user

    @app.route("/users", methods=['GET'])
    def get_users():
        return "HELLO"

    @app.route("/user", methods=['GET'])
    @auth.login_required
    def get_user():
        user = auth.current_user()
        return user['email']
    
    @app.route("/scores", methods=['POST'])
    @auth.login_required
    def save_scores():
        score = request.json.get('score')
        level = request.json.get('level')
        user = auth.current_user()
        email = user['email']
        score_entry = { 'score': score, 'level': level }
        user_scores = scores.get(email)
        if user_scores: 
            user_scores.append(score_entry)
        else:
            scores[email] = [score_entry]
        
        return score_entry

    @app.route("/scores/top", methods=['GET'])
    @auth.login_required
    def get_high_score():
        user = auth.current_user()
        email = user['email']
        user_scores = scores.get(email)
        if user_scores:
            slist = sorted(user_scores, key=lambda se: se['score'], reverse=True)
            return slist[0]
        else:
            return None


