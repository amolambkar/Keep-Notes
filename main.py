'''
author -  Amol Ambkar
Program - Notes Application Main program
'''
from notesapp import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)