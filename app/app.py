import string
import secrets
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def index():
    """ Index page """
    remote_ip = request.environ.get('HTTP_X_FORWARDED_FOR', request.remote_addr)
    return render_template('index.html', remote_ip=remote_ip)

@app.route("/about")
def about():
    """ About page """
    return render_template('about.html')

@app.route("/random")
def random():
    """ Random Page"""
    characters = string.ascii_letters + string.digits + string.punctuation
    random_characters = ''.join(secrets.choice(characters) for i in range(16))
    return render_template('random.html', random_characters=random_characters)
