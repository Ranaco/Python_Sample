from flask import Flask
from flask import render_template 

app = Flask(__name__)

def search4vowels(word:str) ->set:
    vowels = set('aeiou')
    #word = input('Enter any word to detect whether it contains vowels or not : ')
    found = vowels.intersection(set(word))
    return bool(found)

def search4letters(pharse:str, letters:str = 'aeiou') ->set:
    return set(pharse).intersection(set(letters))
    


@app.route('/search')
def sear():
    return str(search4letters('life is a universe'))

@app.route('/')
@app.route('/entry')
def entry_page():
    return render_template('entry.html', the_title="Welcome th search4letters on the web")
app.run()


