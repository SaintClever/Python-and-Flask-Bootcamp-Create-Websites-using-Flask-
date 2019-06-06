from models import db, Teacher, Student, Subject

db.create_all()

mrs_levy = Teacher('Mrs. Levy')
db.session.add(mrs_levy)
db.session.commit()
print(Teacher.query.all())

# mrs_levy = Teacher('Mrs. Levy')
english = Subject('English', mrs_levy)
db.session.add(english)
db.session.commit()
print(Subject.query.all())