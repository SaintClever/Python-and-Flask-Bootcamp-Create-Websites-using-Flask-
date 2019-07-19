from models import db, Teacher, Subject, Student


''' CREATE ''' # Teachers
mrs_brown = Teacher('Mrs. Brown')
mr_burns = Teacher('Mr. Burns')
mrs_jelenich = Teacher('Mrs. Jelenich') 
mrs_levy = Teacher('Mrs. Levy')

# db.session.add_all([
#     mrs_brown,
#     mr_burns,
#     mrs_jelenich,
#     mrs_levy
# ])
# db.session.commit()

''' READ '''
# print(Teacher.query.all())


'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''' 
# Target first instance of teacher


''' CREATE ''' # Subjects
mrs_brown = Teacher.query.filter_by(teacher_name='Mrs. Brown').all()[0]
mr_burns = Teacher.query.filter_by(teacher_name='Mr. Burns').all()[0]
mrs_jelenich = Teacher.query.filter_by(teacher_name='Mrs. Jelenich').first()
mrs_levy = Teacher.query.filter_by(teacher_name='Mrs. Levy').first()

social_studies = Subject('Social Studies', mrs_brown.id)
literature = Subject('Literature', mr_burns.id)
science = Subject('Science', mrs_jelenich.id)
english = Subject('English', mrs_levy.id)

# db.session.add_all([
#     social_studies,
#     literature,
#     science,
#     english
# ])
# db.session.commit()

''' READ '''
# print(Subject.query.all())
print(
    Teacher.query.filter_by(teacher_name='Mrs. Brown').all()[0],
    Teacher.query.filter_by(teacher_name='Mr. Burns').all()[0],
    Teacher.query.filter_by(teacher_name='Mrs. Jelenich').first(),
    Teacher.query.filter_by(teacher_name='Mrs. Levy').first()
)



''' CREATE ''' # Students
alex = Student('Alex Trivet', mrs_jelenich.id)
blake = Student('Blake Budden', mrs_brown.id)
nesta = Student('Nesta Parchment', mrs_levy.id)
zack = Student('Zack Morris', mr_burns.id)

# db.session.add_all([
#     alex,
#     blake,
#     nesta,
#     zack
# ])
# db.session.commit()

# ''' READ ''' # List of students 
'''
We don't need to print them out because we
utilize print() in the models.py file
'''
# print(Student.query.all())
mrs_brown.list_students()
mr_burns.list_students()
mrs_jelenich.list_students()
mrs_levy.list_students()

print('')