# PROBLEM 2
# Create a code maker funtion. This function
# will take in a string name and replace any vowels
# with the letter x.

def code_maker(user_input):
    vowels = ['a','e','i','o','u']
    user_output = []

    # print(''.join(vowels))
    # print(user_input)

    for character in user_input.lower():
        # print(character)
        if character in ''.join(vowels): # in or ==
            # print(character)
            user_output.append('x')
        else:
            user_output.append(character)

    # print(user_output)
    return ''.join(user_output)

result = code_maker('LOVE ME!')
print(result)
