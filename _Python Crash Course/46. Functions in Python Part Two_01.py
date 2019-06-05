# PROBLEM 2
# Create a code maker funtion. This function
# will take in a string name and replace any vowels
# with the letter x.

def code_maker(mystring):

    output = list(mystring) # Turn user input into a list to replace it
    print(output)

    for index,letter in enumerate(mystring): # Go through every letter in a string
    # use enumerate to get index and character
        # print(letter)
        for vowel in 'aeiou': # Check it against every possible vowel
            # print(letter)
            # print(letter == vowel)
            if letter.lower() == vowel:
                print(letter)
                output[index] = 'x' # Set vowel to x

    output = ''.join(output)
    return output

print(code_maker('Sammy and Adam'))
