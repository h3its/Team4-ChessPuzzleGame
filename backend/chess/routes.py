from flask import abort, request, session

def configure_routes(app, auth):

    @auth.verify_password
    def verify_password(email, password):
        if email == "test@test.com":
            return {'email': email, 'password': password}
        else:
            return False

    @app.before_request
    def before_request():
        print("REQUEST...")
        print(request.method, request.endpoint, request.authorization)

    @app.route("/users", methods=['GET'])
    def get_users():
        return "HELLO"

    @app.route("/user", methods=['GET'])
    @auth.login_required
    def get_user():
        user = auth.current_user()
        return user['email']
        

