import os, random
from flask import Flask, request, jsonify, session
from flask_wtf import FlaskForm
from wtforms import validators, DecimalField, StringField
global digit

os.environ["FLASK_RANDOM_SEED"] = "13"
app = Flask(__name__)
app.config.update(
    DEBUG=True,
    SECRET_KEY='myyyyyy_keyyyyyyy',
    WTF_CSRF_ENABLED=False,
)
scope = int(os.environ["FLASK_RANDOM_SEED"])
random.seed(scope)
digit = None


def new_current_number():
    digit = random.randint(1, scope)


@app.route('/', methods=['GET'])
def hidden_number():
    """
    Функция обработки запроса к главной странице
    :return: строка
    """
    new_current_number()
    return "Новое число загадано"


class GuessForm(FlaskForm):
    username = StringField(label='Имя', validators=[
        validators.DataRequired()
    ])
    digit_guess = DecimalField(label='Отгаданное число', validators=[
        validators.DataRequired()
    ])
