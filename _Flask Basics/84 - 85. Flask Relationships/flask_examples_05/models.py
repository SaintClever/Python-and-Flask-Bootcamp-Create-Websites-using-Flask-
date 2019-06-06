import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)

''''''''''''''''''''''''

# class Teacher
class Teacher(db.Model):
    
    __tablename__ = 'teachers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    students = db.relationship('Student', backref='teacher', lazy='dynamic')
    subject = db.relationship('Subject', backref='teacher', uselist=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        if self.subject:
            return f'{self.name} will be teaching {self.subject.subject_name}'
        else:
            return f'{self.name} will not be teaching this semester'

    def report_student(self):
        print('Students this semester:')
        for student in self.students:
            print(student.student_name)


# class Student
class Student(db.Model):
    
    __tablename__ = 'students'

    id = db.Column(db.Integer, primary_key=True)
    student_name = db.Column(db.Text)
    teacher_id = db.Column(db.Integer, db.ForeignKey('teachers.id'))

    def __init__(self, student_name, teacher_id):
        self.student_name = student_name
        self.teacher_id = teacher_id


# class Subject
class Subject(db.Model):
    
    __tablename__ = 'subjects'

    id = db.Column(db.Integer, primary_key=True)
    subject_name = db.Column(db.Text)
    teacher_id = db.Column(db.Integer, db.ForeignKey('teachers.id'))

    def __init__(self, subject_name, teacher_id):
        self.subject_name = subject_name
        self.teacher_id = teacher_id


if __name__ == '__main__':
    app.run(debug=True)