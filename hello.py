from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login/')
def login():
    return render_template('login.html')

@app.route('/profile/',methods=['POST','GET'])
def profile():
    user_name = request.form['user_name']
    password = request.form['password']
    print(user_name,password)
    return render_template('profile.html', user_name=user_name,password=password)
