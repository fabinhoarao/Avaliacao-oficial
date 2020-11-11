from flask import Flask
from flask import render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:Luan2020*#!Miguel@localhost:3306/tecweb'
db = SQLAlchemy(app)

class Cadastrotime(db.Model):
    __tablename__ = "tabelatimes"
    _id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50))
    ano = db.Column(db.String(9))
    titulos = db.Column(db.String(2))
    classtemporada = db.Column(db.String(50))
    
    def __init__(self, nome, ano, titulos, classtemporada):
        self.nome = nome
        self.ano = ano
        self.titulos = titulos
        self.classtemporada = classtemporada

class Cadastropartidas(db.Model):
    __tablename__ = "tabelapartidas"
    _id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    casa = db.Column(db.String(50))
    visitante = db.Column(db.String(50))
    data = db.Column(db.String(10))
    horario = db.Column(db.String(5))
    
    
    def __init__(self, casa, visitante, data, horario):
        self.casa = casa
        self.visitante = visitante
        self.data = data
        self.horario = horario
    
db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/jogosdarodada')
def jogosdarodada():
    return render_template('jogosdarodada.html')

@app.route('/times')
def times():
    return render_template('times.html')

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

@app.route('/cadastropartidas')
def cadastropartidas():
    return render_template('cadastropartidas.html')

@app.route('/cadastroconcluido')
def cadastroconcluido():
    return render_template('cadastroconcluido.html')


@app.route('/cadastrarpartidas', methods=['GET', 'POST'])
def cadastrarpartidas():
    if request.method == 'POST':
        casa = request.form.get('casa')
        visitante  = request.form.get('visitante')
        data = request.form.get('data')
        horario = request.form.get('horario')
        if casa:
            f = Cadastropartidas(casa, visitante, data, horario)
            db.session.add(f)
            db.session.commit()
    return redirect(url_for('cadastroconcluido'))

@app.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():
    if request.method == 'POST':
        nome = request.form.get('nome')
        ano  = request.form.get('ano')
        titulos = request.form.get('titulos')
        classtemporada = request.form.get('classtemporada')
        if nome:
            f = Cadastrotime(nome, ano, titulos, classtemporada)
            db.session.add(f)
            db.session.commit()
    return redirect(url_for('cadastroconcluido'))
    
    
@app.route("/listar")
def listar():
    partidas = Cadastropartidas.query.all()
    return render_template("listar.html", Cadastropartidas=partidas)

@app.route("/listartimes")
def listartimes():
    time = Cadastrotime.query.all()
    return render_template("listartimes.html", Cadastrotime=time)


if __name__ == "__main__":
    app.run(debug=True)
