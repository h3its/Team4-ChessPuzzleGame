import unittest
import uuid
from db import ChessDB

class TestChessDB(unittest.TestCase):
    # String email;
    # ChessDB db;

    def setUp(self):
        self.db = ChessDB(dbname="postgres", user="postgres", password="example", host="localhost", port=5432)

        # Create a test user for score cases
        self.email = str(uuid.uuid4()) + "@bar.com"
        self.db.add_user(self.email, "bar")

    def test_add_user(self):
        email = str(uuid.uuid4()) + "@bar.com"
        self.db.add_user(email, "bar")

        saved_user = self.db.get_user_by_email(email)
        self.assertEqual(saved_user['email'], email)
        self.assertEqual(saved_user['password'], 'bar')

    def test_save_score_once(self):
        """
        Test saving the first score returns the value
        """
        self.db.save_score(self.email, 50, 2)
        saved_score = self.db.get_high_score(self.email)
        self.assertEqual(saved_score['score'], 50)    

    def test_save_lower_score(self):
        """
        Test saving a score, then saving a lower, returns
        the original score
        """
        self.db.save_score(self.email, 50, 2)
        self.db.save_score(self.email, 40, 3)
        saved_score = self.db.get_high_score(self.email)
        self.assertEqual(saved_score['score'], 50)

    def test_save_higher_score(self):
        """
        Test saving a score, then saving a higher score,
        returns the higher score
        """
        self.db.save_score(self.email, 50, 2)
        self.db.save_score(self.email, 60, 3)
        saved_score = self.db.get_high_score(self.email)
        self.assertEqual(saved_score['score'], 60)

    def test_get_high_score_no_scores(self):
        """
        Test getting high score for a user
        without any scores returns None
        """
        saved_score = self.db.get_high_score(self.email)
        self.assertEqual(saved_score, None)

    def test_add_same_user_twice(self):
        email = str(uuid.uuid4()) + "@bar.com"
        self.db.add_user(email, "bar")
        self.db.add_user(email, "bar")
        saved_user = self.db.get_user_by_email(email)
        self.assertEqual(saved_user['email'], email)
        self.assertEqual(saved_user['password'], 'bar')
        
if __name__ == '__main__':
    unittest.main()