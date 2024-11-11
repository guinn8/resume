# main.py

from backend import app
from database import db

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
