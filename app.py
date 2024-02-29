from flask import Flask,render_template
from auth import RegisterUser, LoginUser
import requests

app = Flask(__name__, static_folder='styles')
app.config['SECRET_KEY'] = 'a123a8fe7c2a029cc60e12582d090c35'

url = 'https://swapi.dev/api/films/'
res = requests.get(url=url)
data = res.json()
@app.route('/')
@app.route('/home')
def landingpage():
    return render_template('home.html', contents=data['results'], title='Home')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/login')
def login():
    return render_template('login.html', form=LoginUser())
@app.route('/register')
def register():
    return render_template('register.html', form=RegisterUser())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5020, debug=True)