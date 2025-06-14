from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

# Mock login credentials
USERS = {
    "yatheeswar2007": "1234"
}

@app.route('/login', methods=['GET', 'POST'])

def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if USERS.get(username) == password:
            return redirect(url_for('index'))
        else:
            return "Invalid credentials"

    return render_template('login.html')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=10000)

