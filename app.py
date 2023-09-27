from flask import Flask, render_template, request

import random
import string

app = Flask(__name__)

def generate_password(length):
    characters = string.ascii_letters + string.digits + '$!?&@:'
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

@app.route('/', methods=['GET', 'POST'])
def password_generator():
    password = None
    if request.method == 'POST':
        password_length = int(request.form['password_length'])
        password = generate_password(password_length)
    return render_template('index.html', password=password)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)  # Set use_reloader to False
