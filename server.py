from flask import Flask, render_template, request, session, redirect
from user import User
app = Flask(__name__)
app.secret_key ='dkfdjadsa243kdfdk30303kddkda;fj'

@app.route('/')
def redirect_user():
    return redirect('/users/register')

@app.route('/users/register')
def index():
    return render_template('index.html')


@app.post('/users')
def ninja_user():
    User.validate_user(request.form)
    session['name'] = request.form['name']
    session['location'] =request.form['location']
    session['favorite_lang'] = request.form['favorite_lang']
    session['kind_of_ninja'] = request.form['kind_of_ninja']
    return redirect('/users/register')

@app.get('/users')
def results():
    return render_template('results.html')

# @app.route('/process')

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5001)