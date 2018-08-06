from flask import Flask, request, redirect, render_template, session
import data_manager

app = Flask(__name__)
app.secret_key = "any random string"


@app.route('/')
def planet_list():
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user_name = request.form['user_name']
        password = request.form['password']
        password_again = request.form['password_again']
        if password == password_again:
            data_manager.register(user_name, password)
    return render_template('loginregister.html')


if __name__ == '__main__':
    app.run(
        debug=True,
        port=5000

    )