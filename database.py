from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Startup(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    industry = db.Column(db.String(100))

    name = db.Column(db.String(100))

    idea = db.Column(db.String(200))

    customer = db.Column(db.String(100))

    revenue = db.Column(db.String(100))

    description = db.Column(db.Text)

    score = db.Column(db.Integer)

    favorite = db.Column(db.Boolean, default=False)

    created_at = db.Column(
        db.DateTime,
        server_default=db.func.now()
    )