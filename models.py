from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    age = db.Column(db.Integer)
    grade = db.Column(db.String(50))

class Meal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(20))  # keep string for simplicity
    food_type = db.Column(db.String(200))
    students_served = db.Column(db.Integer)

class HealthRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'))
    date = db.Column(db.String(20))
    weight = db.Column(db.Float)
    height = db.Column(db.Float)
    student = db.relationship("Student", backref="healths", lazy=True)

class Lesson(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    content = db.Column(db.Text)
