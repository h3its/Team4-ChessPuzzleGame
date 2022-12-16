
class InvalidLoginException(Exception):
    pass

class UserNotFoundException(Exception):
    pass

class ChessService:

    def __init__(self):
        self.db = db

    def signup(self, email, password):
        self.db.add_user(email, password)

    def login(self, email, password):
        user = self.db.get_user_by_email(email)
        if not user or user['password'] != password:
            raise InvalidLoginException

    def save_score(self, email, score, level):
        user = self.db.get_user_by_email(email)
        old_score = None
        if self.db.get_high_score(email, level):
            old_score = self.db.get_high_score(email, level)['score']
        print(old_score)
        if user:
            if not old_score:
                self.db.save_score(email, score, level)
            elif score < old_score:
                self.db.update_score(email, score, level)
        else:
            raise UserNotFoundException

    def get_high_score(self, email):
        return self.db.get_high_score(email)

    def get_users(self):
        raw_users = self.db.list_users()
        users = []
        for i in range(len(raw_users)):
            users.append(dict(raw_users[i])['email'])
        return users

    def get_leaders(self, level):
        leaders = self.db.list_leaders(level)
        return leaders



