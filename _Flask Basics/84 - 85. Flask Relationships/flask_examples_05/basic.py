from models import db, Teacher, Subject, Student

# mr_burns = Teacher('Mr. Burns')
# db.session.add(mr_burns)
# db.session.commit()
print(Teacher.query.all())


# mr_burns = Teacher.query.filter_by(name='Mr. Burns').first()
# print(mr_burns)
# math = Subject('Math', mr_burns.id)
# db.session.add(math)
# db.session.commit()
# print(Subject.query.all())

mr_burns = Teacher.query.filter_by(name='Mr. Burns').first()
# print(mr_burns)
adam = Student('Adam', mr_burns.id)
db.session.add(adam)
db.session.commit()
# print(Student.query.all())

mr_burns.report_students()