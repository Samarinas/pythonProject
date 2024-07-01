from flask import Flask, render_template, request, redirect, url_for, flash, session
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Simulação de banco de dados
usuarios = {'usuario': 'senha'}
funcionarios = {'funcionario': 'senha'}
cadastros = []

@app.route('/')
def index():
    return render_template('cadastro.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    if username in usuarios and usuarios[username] == password:
        session['username'] = username
        flash('Login realizado com sucesso!', 'success')
        return redirect(url_for('index'))
    else:
        flash('Usuário ou senha incorretos. Tente novamente.', 'error')
        return redirect(url_for('index'))

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

@app.route('/cadastrar_pcd', methods=['POST'])
def cadastrar_pcd():
    nome = request.form['nome']
    data_nascimento = request.form['data_nascimento']
    email = request.form['email']
    telefone = request.form['telefone']
    sexo = request.form['sexo']
    tipo_deficiencia = request.form['tipo_deficiencia']
    descricao_deficiencia = request.form['descricao_deficiencia']
    cep = request.form['cep']
    endereco = request.form['endereco']
    cidade = request.form['cidade']
    uf = request.form['uf']
    laudo_medico = request.files['laudo_medico']
    if laudo_medico:
        filename = secure_filename(laudo_medico.filename)
        laudo_medico.save(os.path.join('static/uploads', filename))
        cadastro = {
            'nome': nome,
            'data_nascimento': data_nascimento,
            'email': email,
            'telefone': telefone,
            'sexo': sexo,
            'tipo_deficiencia': tipo_deficiencia,
            'descricao_deficiencia': descricao_deficiencia,
            'cep': cep,
            'endereco': endereco,
            'cidade': cidade,
            'uf': uf,
            'laudo_medico': filename
        }
        cadastros.append(cadastro)
        flash('Cadastro realizado com sucesso. Em breve entraremos em contato.', 'success')
    return redirect(url_for('index'))

@app.route('/funcionario')
def funcionario():
    if 'funcionario' in session:
        return render_template('funcionario.html', cadastros=cadastros)
    else:
        return redirect(url_for('func_login'))

@app.route('/func_login', methods=['GET', 'POST'])
def func_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in funcionarios and funcionarios[username] == password:
            session['funcionario'] = username
            flash('Login de funcionário realizado com sucesso!', 'success')
            return redirect(url_for('funcionario'))
        else:
            flash('Usuário ou senha incorretos. Tente novamente.', 'error')
    return render_template('funcionario_login.html')

if __name__ == '__main__':
    app.run(debug=True)
