from flask import Flask, request
from flask_wtf import FlaskForm
from wtforms import StringField, validators

import json
import datetime

locals_list = ['ru', 'en', 'it']

app = Flask(__name__)
app.config.update(
    DEBUG = True,
    SECRET_KEY='This key must be secret!',
    )

class RegForm(FlaskForm):
    email = StringField(validators = [
            validators.Length(min=6, max=36, message="Leght from 6 to 36"),
            validators.Email(message="Wrong e-mail"),
            validators.Required(),
        ])



@app.route('/locales')
def locales():
    return json.dumps(locals_list)

@app.route('/meta')
def meta():
    now_date = datetime.datetime.now()
    print(now_date.month)
    meta_info = { "current_date": now_date.strftime('%d/%m/%Y'),
                  "current_time": now_date.strftime('%H:%M:%S'),
                  "received_headers": True,
                  "received_query_args": ["name", "job", "age"]
                }
    return json.dumps(meta_info)

@app.route('/form/user',methods=["POST"] )
def user_form():
    regform = RegForm(request.form)
    print(regform.vatidate())
    return "ok", 200


if __name__ == "__main__":
    app.run()