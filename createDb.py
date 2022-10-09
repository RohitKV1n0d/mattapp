from app import app, db


def test_connection(self):
    with app.app_context():
        db.create_all() 
        print("Database created")


test_connection(self=None)
