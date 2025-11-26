from flask import Flask, render_template, request, redirect, url_for, flash
from models.pessoa import Pessoa
from controllers.pessoa_controller import PessoaController
from database import db, init_app

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pessoas.db'
import secrets
app.config['SECRET_KEY'] = secrets.token_hex(16)  # Gera uma chave segura
#app.config['SECRET_KEY'] = 'sua_chave_secreta_aqui'

# Inicializa o banco de dados
init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar_pessoa():
    if request.method == 'POST':
        try:
            nome = request.form.get('nome', ' ').strip()
            sobrenome = request.form.get('sobrenome', ' ').strip()
            cpf = request.form.get('cpf', ' ').strip()
            data_nascimento = request.form.get('data_nascimento', ' ').strip()

            if not nome:
                return "Nome é obrigatório", 400
            if not sobrenome:
                return "Sobrenome é obrigatório", 400
            if not cpf:
                return "CPF é obrigatório", 400
            if not data_nascimento:
                return "Data de nascimento é obrigatória", 400
            
            PessoaController.salvar_pessoa(
                nome,
                sobrenome,
                cpf,
                data_nascimento
            )
            # flash('Pessoa cadastrada com sucesso!', 'success')
            # return redirect(url_for('listar_pessoas'))

            #para teste:
            return "Pessoa cadastrada", 200
        
        except Exception as e:
            flash(f'Erro ao cadastrar: {str(e)}', 'danger')
    return render_template('cadastrar.html')

@app.route('/listar')
def listar_pessoas():
    pessoas = Pessoa.query.all()
    return render_template('listar.html', pessoas=pessoas)

@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar_pessoa(id):
    pessoa = Pessoa.query.get_or_404(id)
    if request.method == 'POST':
        try:
            pessoa.nome = request.form['nome']
            pessoa.sobrenome = request.form['sobrenome']
            pessoa.cpf = request.form['cpf']
            pessoa.data_de_nascimento = request.form['data_nascimento']
            db.session.commit()
            flash('Pessoa atualizada com sucesso!', 'success')
            return redirect(url_for('listar_pessoas'))
        except Exception as e:
            flash(f'Erro ao atualizar: {str(e)}', 'danger')
    return render_template('editar.html', pessoa=pessoa)

@app.route('/remover/<int:id>')
def remover_pessoa(id):
    try:
        pessoa = Pessoa.query.get_or_404(id)
        db.session.delete(pessoa)
        db.session.commit()
        flash('Pessoa removida com sucesso!', 'success')
    except Exception as e:
        flash(f'Erro ao remover: {str(e)}', 'danger')
    return redirect(url_for('listar_pessoas'))

if __name__ == '__main__':
    app.run(debug=True)