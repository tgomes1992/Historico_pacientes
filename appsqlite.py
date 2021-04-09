from flask import Flask , render_template,request,redirect,url_for,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import sys
from datetime import datetime
import sqlite3





#app configuration

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = r'sqlite:///D:\Projects\clientes\Historico_pacientes\foo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

migrate = Migrate(app, db)

#class definitions objects definition

class Cliente(db.Model):
    id = db.Column(db.Integer(),primary_key=True)
    nome =  db.Column(db.String(),nullable=False)
    data_nascimento = db.Column(db.Date())
    email = db.Column(db.String())
    telefone = db.Column(db.String())
    endereco = db.Column(db.String())
    bairro = db.Column(db.String())
    saude = db.relationship("Saude",backref='dados_saude')
    visitas = db.relationship("Visitas",backref='visitas')
    def __repr__(self):
         return f'<Person ID: {self.id}, nome: {self.nome}>'

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


#help functions

def manipula_data(data):
    periodo = date(data) + timedelta(days=30)
    periodo_traduzido = periodo.strftime('%d/%m/%Y')
    return periodo_traduzido

def date_sql(data):
    str = data
    ndate = datetime.strptime(data,'%Y-%m-%d').date()
    return ndate

def date_sql2(data):
    str = data
    ndate = datetime.strptime(data,'%d/%m/%Y').date()
    return ndate



#routes

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/client_list',methods=['POST','GET'])
def client_list():

    
    client = Cliente.query.all()
    nclient = []
    response = request.form.get('value')

    if response == None:
        nclient = Cliente.query.all()
    else:
        for i in client:
            ndict = {}
            if  response.casefold() in i.nome.casefold():
                #print(i.nome)
                ndict['id'] = i.id
                ndict['nome'] = i.nome
                nclient.append(ndict)        
    return render_template("client_list.html",clientes=nclient)

@app.route('/client_list/search',methods=['POST','GET'])
def find_client():

    response = request.form.get("value")
    client = Cliente.query.all()
    nclient = []
    nomes = []
    if response != None:
        for i in client:
            
            if  response.casefold() in i.nome.casefold():
                ndict = {}
                print(i.nome)
                ndict['id'] = i.id
                ndict['nome'] = i.nome
                nclient.append(ndict)
    
    print(response)
        
 
    return render_template("search_client.html",clientes=nclient)

@app.route('/main')
def index2():
    return render_template("cadastro.html")

@app.route('/verificar/paciente/',methods=['GET'])
def checar_paciente():
    response = request.values['id']
    print(response)
    modificado = Cliente.query.get(response)
    resposta = {
        'id':modificado.id,         
        'nome_completo':modificado.nome,
        'nascimento':modificado.data_nascimento,  
        'email': modificado.email,
        'telefone'  : modificado.telefone,
        'endereco':modificado.endereco,
        'bairro':modificado.bairro,
    }
    print(modificado)
    return resposta

@app.route('/cadastrar/paciente',methods=['POST'])
def cadastrar_pacientes():

    npaciente = request.get_json()
    print(npaciente['nascimento'])
    ndate = date_sql(npaciente['nascimento'])
    paciente = Cliente(nome=npaciente['nome'],
                data_nascimento=ndate,
                email=npaciente['email'],
                telefone=npaciente['telefone'],
                endereco=npaciente['endereco'],
                bairro=npaciente['bairro'])
    #print(paciente)
    db.session.add(paciente)
    db.session.commit()
    print(paciente)





    # try:
    #     npaciente = request.get_json()
    #     print(npaciente)
    #     paciente = Cliente(nome=npaciente['nome'],data_nascimento=npaciente['nascimento'],email=npaciente['email'],telefone=npaciente['telefone'],endereco=npaciente['endereco'],bairro=npaciente['bairro'])
    #     #print(paciente)
    #     db.session.add(paciente)
    #     db.session.commit()
    #     print(paciente)
    # except:
    #     db.session.rollback()
    # finally:
    #     db.session.close()  
    return redirect(url_for('client_list'))

@app.route('/excluir/paciente',methods=['POST'])
def excluir_paciente():
    try:
        idcliente = request.values['id']
        Visitas.query.filter_by(paciente_id=idcliente).delete()
        Cliente.query.filter_by(id=idcliente).delete()
        db.session.commit()
    except:
        db.session.rollback()
    finally:
        db.session.close()
    return redirect(url_for('index2'))

@app.route('/modificar/pacientes',methods=['POST'])
def modificar_paciente():
    id = request.values['id']
    print(id)
    cliente = Cliente.query.get(id)
    cliente.data_nascimento = date_sql(request.values['data_nascimento'])
    cliente.email = request.values['email']
    cliente.telefone = request.values['telefone']
    cliente.endereco = request.values['endereco']
    cliente.bairro = request.values['bairro']
    cliente.nome = request.values['nome']
    db.session.commit()
    db.session.close()
    return redirect(url_for('client_list'))

@app.route('/visita/<id>')
def visita_paciente(id):
    return render_template("visitas.html",visitas_check = Visitas.query.filter_by(paciente_id=id),nome = Cliente.query.get(id))

@app.route('/visita/paciente/<id>/registrar',methods=['POST'])
def visita_paciente_registrar(id):
    resposta = request.values
    recebido = Cliente.query.get(id)
    pdata = date_sql2(resposta['data'])
    nvisita =Visitas(data=pdata,estado_inicial=resposta['inicial'],estado_final=resposta['final'],proxima_visita=pdata,paciente_id=id)
    db.session.add(nvisita)
    db.session.commit()
    db.session.close()
    return visita_paciente(id)



if __name__:"__main__"
app.run(debug=True)

