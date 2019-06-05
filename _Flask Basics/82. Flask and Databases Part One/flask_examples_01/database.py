from basic import Human, db

db.create_all()


jennifer = Human('Jennifer Ngo', 24, 'Vietnamese')
nesta = Human('Nesta Parchment', 35, 'Jamaican-American')
dee = Human('Dee Budden', 38, 'American')


db.session.add_all([jennifer, nesta, dee])

db.session.commit()


print(jennifer.id)
print(jennifer)
print('')

print(nesta.id)
print(nesta)
print('')

print(dee.id)
print(dee)