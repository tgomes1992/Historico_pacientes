from flask import Flask , render_template,request,redirect,url_for,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import sys


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:tAman1993**@localhost:5432/podologia'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

migrate = Migrate(app, db)

#classes modelos

class Cliente(db.Model):
    id = db.Column(db.Integer(),primary_key=True)
    nome_completo =  db.Column(db.String(),nullable=False)
    data_nascimento = db.Column(db.Date())
    email = db.Column(db.String())
    telefone = db.Column(db.String())
    endereco = db.Column(db.String())
    bairro = db.Column(db.String())
    saude = db.relationship("Saude",backref='dados_saude')
    visitas = db.relationship("Visitas",backref='visitas')
    # def __repr__(self):
    #     return f'<Person ID: {self.id}, nome: {self.nome_completo}>'

class Saude(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    diabetes = db.Column(db.Boolean(),nullable=False)
    alergia = db.Column(db.Boolean(),nullable=False)
    cliente_id = db.Column(db.Integer(), db.ForeignKey('cliente.id'),nullable=False)
    cliente = db.relationship("Cliente",back_populates="saude")

class Visitas(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    data = db.Column(db.Date())
    estado_inicial=db.Column(db.String())
    estado_final=db.Column(db.String())
    proxima_visita = db.Column(db.Date())
    paciente_id = db.Column(db.Integer(), db.ForeignKey('cliente.id'),nullable=False)



db.create_all()


#rotas

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/client_list')
def client_list():
    return render_template("client_list.html",clientes=Cliente.query.all())


@app.route('/main')
def index2():
    return render_template("main.html")


#crud cliente

@app.route('/verificar/paciente/<cliente_id>',methods=['GET'])
def checar_paciente(cliente_id):
    modificado = Cliente.query.get(cliente_id)
    resposta = {
        'id':modificado.id,
        'nome_completo':modificado.nome_completo,
        'nascimento':modificado.data_nascimento,
        'email': modificado.email,
        'telefone'  : modificado.telefone,
        'endereco':modificado.endereco,
        'bairro':modificado.bairro,
    }
    return resposta



@app.route('/cadastrar/paciente',methods=['POST'])
def cadastrar_pacientes():
    try:
        npaciente = request.get_json()
        paciente = Cliente(nome_completo=npaciente['nome'],data_nascimento=npaciente['nascimento'],email=npaciente['email'],telefone=npaciente['telefone'],endereco=npaciente['endereco'],bairro=npaciente['bairro'])
        db.session.add(paciente)
        db.session.commit()
    except:
        db.session.rollback()
    finally:
        db.session.close()
    return redirect(url_for('client_list'))



@app.route('/excluir/paciente',methods=['POST'])
def excluir_paciente():
    try:
        resposta= request.get_json()['nome']
        Cliente.query.filter_by(nome_completo=resposta).delete()
        db.session.commit()
    except:
        db.session.rollback()
    finally:
        db.session.close()
    return redirect(url_for('index2'))


@app.route('/modificar/pacientes',methods=['POST'])
def modificar_paciente():
    id =  request.values['id']
    cliente = Cliente.query.get(id)
    cliente.data_nascimento = request.values['data_nascimento']
    cliente.email = request.values['email']
    cliente.telefone = request.values['telefone']
    cliente.endereco = request.values['endereco']
    cliente.bairro = request.values['bairro']
    cliente.nome_completo = request.values['nome']
    db.session.commit()
    db.session.close()
    return redirect(url_for('index2'))
    #try:


        # cliente.nome_completo=resposta['nome']
        # cliente.data_nascimento =resposta['nascimento']
        # cliente.telefone = resposta['telefone']
        # cliente.endereco = resposta['endereco']
        # cliente.bairro =resposta['bairro']
        #db.session.commit()
    #except:
        #db.session.rollback()
    #finally:
        #db.session.close()



if __name__:"__main__"
app.run(debug=True)

