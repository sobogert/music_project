from flask import Flask, render_template

app = Flask("music project")

@app.route('/')
def hello():
    return render_template('main.html')

