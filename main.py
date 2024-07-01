from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/')
def index():
    return render_template('cadastro.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if username == 'usuario' and password == 'senha':
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
        laudo_medico.save('uploads/' + laudo_medico.filename)

    flash('Cadastro realizado com sucesso. Em breve entraremos em contato.', 'success')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
