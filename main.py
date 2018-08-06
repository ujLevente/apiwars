from flask import Flask, request, redirect, render_template, session
import data_manager

app = Flask(__name__)
app.secret_key = "any random string"


@app.route('/')
def planet_list():
    return render_template('index.html')


@app.route('/register')
def register():
    pass


if __name__ == '__main__':
    app.run(
        debug=True,
        port=5000

    )