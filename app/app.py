from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def index():
    remote_ip = request.environ.get('HTTP_X_FORWARDED_FOR', request.remote_addr)
    return render_template('index.html', remote_ip=remote_ip)

@app.route("/about")
def about():
    return render_template('about.html')
