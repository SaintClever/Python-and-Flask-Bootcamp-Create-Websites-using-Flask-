from basic import Human, db

# people = Human.query.all()
# print(people)

### CREATE
# gabe = Human('Gabriel Then', 30, 'Dominican/ Puerto Rican')
# db.session.add(gabe)
# db.session.commit()


## READ with all()
# everybody = Human.query.all()
# print(everybody)
# print('')

### READ with get
# person_1 = Human.query.get(1)
# print(person_1)

# person_2 = Human.query.get(2)
# print(person_2)

# person_3 = Human.query.get(3)
# print(person_3)

### READ with Filter
filter_by_name = Human.query.filter_by(name='Nesta Parchment')
print(filter_by_name.all())

filter_by_nationality = Human.query.filter_by(nationality='Vietnamese')
print(filter_by_nationality.all())

filter_by_age = Human.query.filter_by(age=30)
print(filter_by_age.all())

filter_by_name_age = Human.query.filter_by(name='Dee Budden', age=38)
print(filter_by_name_age.all())
print('')

### UPDATE - Turn Gabe into Wuan
gabe_to_juan = Human.query.get(3)
gabe_to_juan.name = 'Wuan Bonilla'
gabe_to_juan.age = '35'
gabe_to_juan.nationality = 'Puerto Rican/ Dominican/ American'
db.session.add(gabe_to_juan)
db.session.commit()

print(Human.query.all())
print('')

print(Human.query.get(4))
print('')

delete_gabriel = Human.query.get(4)
db.session.delete(delete_gabriel)

print(Human.query.all())
print('')

print(Human.query.get(4))