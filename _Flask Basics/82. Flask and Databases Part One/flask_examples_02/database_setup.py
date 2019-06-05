from basic import Character, db

db.create_all()


deadpool = Character('Deadpool', 'Marvel Universe', 'This is my taunt! Heh! Get it?', 'Katana-Rama!', 'Trigger Happy (Guns)')

wolverine = Character('Wolverine', 'Marvel Universe', "Nice an' sharp, alright.", 'Berserker Barrage', 'Weapon X')

spiderman = Character('Spiderman', 'Marvel Universe', 'Dude, you SUCK!', 'Maximum Spider', 'Ultimate Web Throw')

db.session.add_all([deadpool,wolverine,spiderman])
db.session.commit()

all_characters = Character.query.all()
print(all_characters)