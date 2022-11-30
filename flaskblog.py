from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '67898466d55cfcc31821aaa4effad47b'

@app.route("/")
@app.route("/index")
@app.route("/home")
def home():
    return render_template('/home.html')

@app.route("/about")
def about():
    return render_template('/about.html')

@app.route("/links")
def links():
    return render_template('/links.html')

@app.route("/gallery")
def gallery():
    return render_template('/gallery.html')

@app.route("/devlog")
def devlog():
    return render_template('/devlog.html')

if __name__ == "__main__":
    app.run(debug=True)