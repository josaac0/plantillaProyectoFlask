## Crear formulario en html, (plantilla html y endpoint en main)
~~~
{% extends "base_template.html" %}

{% block title %}Registro de usuarios{% endblock %}

{% block content %}
    <form action="" method="post">
        <label for="name">Nombre: </label>
        <input type="text" id="name" name="name" /><br>
        <label for="email">Email: </label>
        <input type="text" id="email" name="email" /><br>
        <label for="password">Contraseña: </label>
        <input type="password" id="password" name="password" /><br>
        <input type="submit" id="send-signup" name="signup" value="Registrar" />
    </form>
{% endblock %}
~~~

## Metodo no permitido, agregar la propiedad methods en la vista
~~~
@app.route("/registroForm/", methods=["GET", "POST"])
def registroForm():
    return render_template("registroForm.html")
~~~

## Importar librerias de objetos
~~~
from flask import render_template, request, redirect, url_for
~~~

## Integrar la programación para leer los datos del formulario
~~~
if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        next = request.args.get('next', None)
        if next:
            return redirect(next)
        return redirect(url_for('index'))
~~~

## Instalar wtform con el entorno virtual aislado
~~~
pip install Flask-WTF
pip install email-validator
~~~

## Crear un archivo registerForms.py (touch registerForms.py) y copiar la estructura sig
~~~
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, Length


class registerForm(FlaskForm):
    name = StringField('Nombre', validators=[DataRequired(), Length(max=64)])
    password = PasswordField('Password', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Registrar')
~~~

## Actualizar el template con flaskForm
~~~
{% extends "base_template.html" %}
{% block title %}Registro de usuarios{% endblock %}
{% block content %}
    <form action="" method="post" novalidate>
        {{ form.hidden_tag() }}
        <div>
            {{ form.name.label }}
            {{ form.name(size=64) }}<br>
            {% for error in form.name.errors %}
            <span style="color: red;">{{ error }}</span>
            {% endfor %}
        </div>
        <div>
            {{ form.email.label }}
            {{ form.email }}<br>
            {% for error in form.email.errors %}
            <span style="color: red;">{{ error }}</span>
            {% endfor %}
        </div>
        <div>
            {{ form.password.label }}
            {{ form.password }}<br>
            {% for error in form.password.errors %}
            <span style="color: red;">{{ error }}</span>
            {% endfor %}
        </div>
        <div>
            {{ form.submit() }}
        </div>
    </form>
{% endblock %}
~~~

## Actualizar el back
~~~
from registroForms import registerForm
@app.route("/registroForm/", methods=["GET", "POST"])
    
def registroForm():
    form = registerForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        password = form.password.data
        next = request.args.get('next', None)
        if next:
            return redirect(next)
        return redirect(url_for('login'))
    return render_template("registroForm.html",form=form)
~~~