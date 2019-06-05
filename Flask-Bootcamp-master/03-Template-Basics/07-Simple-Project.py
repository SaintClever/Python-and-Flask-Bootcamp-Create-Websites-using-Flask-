# Set up your imports and your flask app.

@app.route('/')
def index():
    # This home page should have the form.
    pass


# This page will be the page after the form
@app.route('/report')
def report():
    # Check the user name for the 3 requirements.

    # HINTS:
    # https://stackoverflow.com/questions/22997072/how-to-check-if-lowercase-letters-exist/22997094
    # https://stackoverflow.com/questions/26515422/how-to-check-if-last-character-is-integer-in-raw-input

    # Return the information to the report page html.
    pass

if __name__ == '__main__':
    # Fill this in!
    pass
