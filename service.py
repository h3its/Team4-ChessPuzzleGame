
class InvalidLoginException(Exception):
    pass

class UserNotFoundException(Exception):
    pass

class ChessService:

    def __init__(self, db):
        self.db = db

    def signup(self, email, password):
        self.db.add_user(email, password)

    def login(self, email, password):
        user = self.db.get_user_by_email(email)
        if not user or user['password'] != password:
            raise InvalidLoginException

    def save_score(self, email, score, level):
        user = self.db.get_user_by_email(email)
        if user:
            self.db.save_score(email, score, level)
        else:
            raise UserNotFoundException

    def get_high_score(self, email):
        return self.db.get_high_score(email)



