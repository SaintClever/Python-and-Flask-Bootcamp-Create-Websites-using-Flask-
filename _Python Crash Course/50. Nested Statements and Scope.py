# LEGB RULE - Order of operations which python calls variables / functions
# LOCAL
# ENCLOSING
# GLOBAL
# BUILT IN

x = 'outside'
def report():
    x = 'inside'
    return x

print(report()) # inside
print(x) # outside
print('')


x = 'THIS IS GLOBAL LEVEL'
def enclosing():
    x = 'Enclosing Level'

    def inside():
        print(x)
    inside()

print(enclosing()) # Enclosing Level
print('')


x = 'THIS IS GLOBAL LEVEL'
def enclosing():
    # x = 'Enclosing Level'

    def inside():
        print(x)
    inside()

print(enclosing()) # THIS IS GLOBAL LEVEL
print('')


x = 'THIS IS GLOBAL LEVEL'
def enclosing():
    x = 'Enclosing Level'

    def inside():
        x = 'Local'
        print(x)
    inside()

print(enclosing()) # Local
print('')


x = 'outside'

def report():
    global x # global method - python use the global x not the inside x variable
    x = 'inside'
    return x
print(report())
print(x)
