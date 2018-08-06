from flask import Flask, request, redirect, render_template, session


app = Flask(__name__)
app.secret_key = "any random string"


@app.route('/')
def mainpage():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(
        debug=True,
        port=5000

    )