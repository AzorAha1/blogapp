from flask import Flask,render_template
import requests

app = Flask(__name__, static_folder='styles')
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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5020, debug=True)