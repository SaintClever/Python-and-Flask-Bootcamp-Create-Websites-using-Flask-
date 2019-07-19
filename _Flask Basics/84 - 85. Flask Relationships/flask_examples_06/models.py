import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)


'''''''''''''''''''''''' # Models

# class Teacher
class Teacher(db.Model):

    __tablename__ = 'teachers'

    id = db.Column(db.Integer, primary_key=True)
    teacher_name = db.Column(db.Text)
    students = db.relationship('Student', backref='teacher', lazy='dynamic')
    subject = db.relationship('Subject', backref='teacher', uselist=False)

    def __init__(self, teacher_name):
        self.teacher_name = teacher_name

    def __repr__(self):
        if self.subject:
            return f'\n{self.teacher_name} will be teaching {self.subject.subject_title} this semester.'
        else:
            return f'\n{self.teacher_name} will not be teaching this semester.'

    def list_students(self):
        print(f'\nStudents taking {self.subject.subject_title}:')
        for student in self.students:
            print(student.student_name)


# class Subject
class Subject(db.Model):
    
    __tablename__ = 'subjects'

    id = db.Column(db.Integer, primary_key=True)
    subject_title = db.Column(db.Text)
    teacher_id = db.Column(db.Integer, db.ForeignKey('teachers.id')) # connect to teachers table

    def __init__(self, subject_title, teacher_id):
        self.subject_title = subject_title
        self.teacher_id = teacher_id


# class Student
class Student(db.Model):
    
    __tablename__ = 'students'

    id = db.Column(db.Integer, primary_key=True)
    student_name = db.Column(db.Text)
    teacher_id = db.Column(db.Integer, db.ForeignKey('teachers.id')) # connect to teachers table

    def __init__(self, student_name, teacher_id):
        self.student_name = student_name
        self.teacher_id = teacher_id


if __name__ == '__main__':
    app.run(debug=True)