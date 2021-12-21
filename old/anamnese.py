from flask import Flask , render_template
from flask_sqlalchemy import SQLAlchemy
from database import cadastro
from database import db,app

# class Retorno(db.model):
#     data = db.column(db.datetime(2020,8,27),nullable=True)


#funções banco de dados


db.session.close()
db.create_all()

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/main')
def index2():
    return render_template("main.html")


app.run(debug=True,host="0.0.0.0")

