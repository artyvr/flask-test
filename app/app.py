from flask import Flask, request, render_template
import random
import string
import secrets

app = Flask(__name__)

@app.route("/")
def index():
    remote_ip = request.environ.get('HTTP_X_FORWARDED_FOR', request.remote_addr)
    return render_template('index.html', remote_ip=remote_ip)

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/random")
def random():
    characters = string.ascii_letters + string.digits + string.punctuation
    random_characters = ''.join(secrets.choice(characters) for i in range(16))
    return render_template('random.html', random_characters=random_characters)
