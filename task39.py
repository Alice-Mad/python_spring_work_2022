from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:mercury1960@localhost:5432/postgres_32'

db = SQLAlchemy(app)


# Students (Child)
class Student(db.Model):
    __tablename__ = 'student_32'
    id_student = db.Column(db.Integer, primary_key=True)
    id_group = db.Column(db.ForeignKey('group_32.id_group'))
    login = db.Column(db.String)
    password = db.Column(db.String)
    surname = db.Column(db.String)
    name = db.Column(db.String)
    email = db.Column(db.String)


# Groups (Parent)
class Group(db.Model):
    __tablename__ = 'group_32'
    id_group = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    students = db.relationship('Student', backref='group_32')

db.create_all()
