from flask import Flask, url_for, redirect, render_template

app = Flask(__name__)
app.debug = True

@app.route('/')
def home():
    return render_template('home.html')


if __name__ == '__main__':
    app.run()