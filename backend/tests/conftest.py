import pytest

@pytest.fixture(scope="session")
def app():
    import os
    os.environ['FLASK_SQLALCHEMY_DATABASE_URI']='sqlite:///:memory:'
    os.environ['FLASK_SECRET_KEY']='changeme'

    from chess import app
    return app

@pytest.fixture
def sample_user():
    from chess import password_hasher
    from chess import db
    from chess.models import User

    try:
        user = User(email='testx@testx.com', password=password_hasher.hash('password'))
        db.session.add(user)
        db.session.commit()
    except:
        db.session.rollback()

    return user
    