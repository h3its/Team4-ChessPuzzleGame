import unittest
import uuid
from db import ChessDB
from service import InvalidLoginException, UserNotFoundException, ChessService

class TestChessService(unittest.TestCase):

    def setUp(self):
        db = ChessDB(dbname="postgres", user="postgres", password="example", host="localhost", port=5432)
        self.service = ChessService(db)

    def test_signup(self):
        email = str(uuid.uuid4()) + "@bar.com"
        self.service.signup(email, "bar")
        self.service.login(email, 'bar')

    def test_login_user_not_found(self):
        email = str(uuid.uuid4()) + "@bar.com"
        with self.assertRaises(InvalidLoginException):
            self.service.login(email, 'foo')
    
    def test_save_score(self):
        email = str(uuid.uuid4()) + "@bar.com"
        self.service.signup(email, "bar")
        self.service.save_score(email, 50, 2)
        score = self.service.get_high_score(email)
        self.assertEqual(score['score'], 50)

    def test_save_score_user_not_found(self):
        email = str(uuid.uuid4()) + "@bar.com"
        with self.assertRaises(UserNotFoundException):
            self.service.save_score(email, 50, 2)

    def test_get_high_score_user_not_found(self):
        email = str(uuid.uuid4()) + "@bar.com"
        self.assertIsNone(self.service.get_high_score(email))

if __name__ == '__main__':
    unittest.main()