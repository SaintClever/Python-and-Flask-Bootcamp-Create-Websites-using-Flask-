d = {'key1':'value1', 'key2':'value2'}
print(d)
print(d['key1'])
print('')

salaries = {'John':20,'Sally':30,'Sammy':15}
print(salaries['Sally'])
salaries['Cindy'] = 100
print(salaries)
print(salaries['Cindy'])
print('')

# John got an raise
salaries['John'] = salaries['John'] + 40
print(salaries)
print(salaries['John'])
print('')

people = {'John':[1,2,3], 'Sally':[40,10,30]}
print(people['John'])
print(people['Sally'][0])
print('')

people = {'John':{'Salary':10, 'age':30}}
print(people['John'])
print(people['John']['age'])
print(people['John']['Salary'])
print('')

d = {'k1':10, 'k2':20, 'k3':30}
print(d.keys())
print(d.values())
print(d.items())
