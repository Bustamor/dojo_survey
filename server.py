from flask import Flask, render_template, request, session, redirect
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
    session['name'] = request.form['name']
    session['location'] =request.form['location']
    session['favorite_lang'] = request.form['favorite_lang']
    session['kind_of_ninja'] = request.form['kind_of_ninja']
    session['first_check'] = request.form['first_check']
    session['second_check'] = request.form['second_check']
    return redirect('/users')

@app.get('/users')
def results():
    return render_template('results.html')

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5001)