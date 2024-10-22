from flask import Flask
from flask import render_template, request, redirect, url_for
from registerForm import registerForm

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta'
@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/registroForm/", methods=["GET", "POST"])
def registroForm():
    form = registerForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        password = form.password.data
        next = request.args.get('next', None)
        print(name)
        print(password)
        print(email)
        if next:
            return redirect(next)
        return redirect(url_for('hello'))
    return render_template("index.html",form=form)