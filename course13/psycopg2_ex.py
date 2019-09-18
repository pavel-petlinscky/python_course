# -*- coding: utf-8 -*-

from datetime import date

from flask import Flask, request
from flask_wtf import FlaskForm
from wtforms import validators, fields

import psycopg2

try:
    conn = psycopg2.connect(
        user='tceh',
        database='frii_db',
        host='localhost',
        password='123',
        port=5432,
    )
except Exception as ex:
    print('I am unable to connect to the database', ex)
    raise ex

app = Flask(__name__)
app.config.update({
    'DEBUG': True,
    'SECRET_KEY': 'very-secret',
    'WTF_CSRF_ENABLED': False,
})


class ObservationForm(FlaskForm):
    observation_date = fields.DateField(default=date.today)
    people_available = fields.IntegerField(
        validators=[
            validators.NumberRange(min=0),
        ]
    )


@app.route('/', methods=['GET', 'POST'])
def index():
    cur = conn.cursor()

    if request.method == 'POST':
        form = ObservationForm(request.form)
        if form.validate():
            od, pa = form.observation_date.data, form.people_available.data
            # YOU SHOULD NEVER DO THIS!
            # cur.execute(
            #     "INSERT INTO public.observations(people_available) "
            #     #"VALUES ('%s');" % pa  # NEVER -> pa = "'); DROP DATABASE ...; SELECT * from ('..."
            #     #"VALUES (''); DROP DATABASE; INSERT INTObbb ('');" % pa  # NEVER -> pa = "'); DROP DATABASE ...; SELECT * from ('..."
            # )

            # Do this instead:
            cur.execute(
                """INSERT INTO public.observations(
                    observation_date, people_available) VALUES (
                    %(observation_date)s, %(people_available)s)""",

                {'observation_date': od.strftime('%Y-%m-%d'),
                 'people_available': pa}
            )
            #conn.rollback()
            conn.commit()  # why do we need this line?
            return str('posted')
        else:
            return str(form.errors)
    else:
        cur.execute(
            """SELECT * from public.observations;"""
            # """SELECT * from public.observations LIMIT 3;"""
            # """SELECT id from public.observations LIMIT 10;"""
            # """SELECT id from public.observations ORDER BY id DESC LIMIT 10 ;"""
        )
        data = cur.fetchall()  # note, that we are fetching the data here.
        return str(data)


if __name__ == '__main__':
    app.run(debug=True)
