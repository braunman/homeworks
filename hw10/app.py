from flask import Flask, request
from flask_wtf import FlaskForm
from wtforms import StringField, validators, PasswordField

import os
import json
import datetime

locals_list = ['ru', 'en', 'it']

app = Flask(__name__)
app.config.update(
    DEBUG=True,
    SECRET_KEY='WWWHHHHHHOOOOOOOOOOOOTTTTTTTTT',
    WTF_CSRF_ENABLED=False,
)


class RegForm(FlaskForm):
    email = StringField(label='E-mail', validators=[
        validators.Length(min=6, max=35), validators.Email()
    ])
    password = PasswordField(validators=[
        validators.EqualTo(fieldname='password2'),
        validators.Length(min=6),
        validators.Required(),
    ])
    password2 = PasswordField('Repeat Password')


@app.route('/locales')
def locales():
    return json.dumps(locals_list)


@app.route('/meta')
def meta():
    now_date = datetime.datetime.now()
    meta_info = {"current_date": now_date.strftime('%d/%m/%Y'),
                 "current_time": now_date.strftime('%H:%M:%S'),
                 "received_headers": dict(request.headers),
                 "received_query_args": dict(request.args),
                 }
    return json.dumps(meta_info, sort_keys=True, indent=4)


@app.route('/form/user', methods=["POST"])
def user_form():
    res = {}
    regform = RegForm(request.form)
    print(request.form, regform.validate())
    if regform.validate():
        res["Status"] = int(regform.validate())
        return json.dumps(res)
    else:
        return json.dumps(regform.errors)


@app.route('/serve/<path:filename>')
def find(filename):
    try:
        with open(os.path.join("./file", filename)) as file:
            return file.read()
    except:
        return 'fail', 404


if __name__ == "__main__":
    app.run()
