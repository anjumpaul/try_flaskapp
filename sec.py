from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def sec():
    #return 'Hello, World!  '+name
    return render_template('sec1.html')
