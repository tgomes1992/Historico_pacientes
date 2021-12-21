from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:tAman1993**@localhost:5432/podologia'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Cliente(db.Model):
    id = db.Column(db.Integer(),primary_key=True)
    nome =  db.Column(db.String(),nullable=False)
    idade = db.Column(db.Integer())
    telefone = db.Column(db.String())
    endereco = db.Column(db.String())
    bairro = db.Column(db.String())
    saude = db.relationship("Saude")
    def __repr__(self):
        return f'<Person ID: {self.id}, nome: {self.nome}, idade: {self.idade}>'

class Saude(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    diabetes = db.Column(db.String())
    acido = db.Column(db.String())
    gravidez = db.Column(db.String())
    hipertenso = db.Column(db.String()) 
    micropgmentacao = db.Column(db.String())
    alergiaanestesico = db.Column(db.String())
    quimioterapia = db.Column(db.String())
    quimioterapia_tempo = db.Column(db.String())
    cliente_id = db.Column(db.Integer(), db.ForeignKey('cliente.id'),nullable=False)
    #cliente = db.relationship("Cliente",back_populates="saude")


def cadastro():
    person1 = Cliente(nome="Thiago",idade=27,telefone=10,endereco='Rua Paulo Santa Helena',bairro="cg")
    db.session.add(person1)
    db.session.commit()
    clientesaude(person1.id)


def clientesaude(id):
    saude = Saude(diabetes="Sim",acido="sim",gravidez="não",hipertenso="sim",micropgmentacao="sim",alergiaanestesico="sim",quimioterapia="sim",quimioterapia_tempo="sim",cliente_id=id)
    db.session.add(saude)
    db.session.commit()


