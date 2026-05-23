from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    name  = "Alex Zhao"
    return render_template('index.html', name=name)

@app.route('/about')
def about():
    return render_template('about.html')

app.run(debug=True)
