from flask import Flask, render_template, request, redirect, url_for, request_finished, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, create_engine, text, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from dotenv import find_dotenv, load_dotenv
from os import getenv, environ


app = Flask(__name__)


dotenv_path = find_dotenv()
load_dotenv(dotenv_path)


engine = create_engine('postgresql+psycopg2://', echo=True, query_cache_size=0,
                       connect_args=dict(host=environ.get("POSTGRES_HOST"), user=environ.get("POSTGRES_USER"),
                                         password=environ.get("POSTGRES_PASSWORD"), database=environ.get("POSTGRES_DATABASE")))


Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

database_uri = f'postgresql+psycopg2://{getenv("POSTGRES_USER")}:{getenv("POSTGRES_PASSWORD")}@{getenv("POSTGRES_HOST")}/{getenv("POSTGRES_DATABASE")}'
app.config['SQLALCHEMY_DATABASE_URI'] = database_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False        #default é True
app.config['SECRET_KEY'] = getenv('SECRET_KEY')

db = SQLAlchemy(app)


class User(Base, UserMixin):
    __tablename__ = 'tb_users_vercel'

    id = Column(Integer, primary_key=True)
    email = Column(String(80), nullable=False)
    senha = Column(String(80), nullable=False)


class Post(Base):
    __tablename__ = 'tb_posts_planet'

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_user = Column(ForeignKey('tb_users_planet.id'))
    titulo = Column(String(80), nullable=False)
    texto = Column(String(244), nullable=False)
    data = Column(DateTime, nullable=False)


#Base.metadata.create_all(engine)


@app.route('/')
def index():
    computer2 = request.environ['REMOTE_ADDR']
    print('computer2 -->', computer2)
    return render_template('index.html')


@app.route('/login')
def login():
    return redirect('/')


@app.route('/user/<int:id>', methods=['GET', 'POST'])
@login_required
def user(id):
    id = id
    print(id)
    conn = engine.connect()
    query_posts = conn.execute(f"select * from tb_posts_rail where id_user = {id}")
    #conn.execute(f"insert into tb_posts_rail values(default, '{id}', 'titulo 7', 'texto 7', '{datetime.utcnow()}')")
    return render_template('user.html', id=id, query_posts=query_posts)


@app.route('/add', methods=['GET', 'POST'])
def add_user():

    email = request.form.get('name_email')
    senha = request.form.get('name_senha')
    new_user = User(email=email, senha=senha)
    print('')
    print(f'funcao add_user \n \n'
          f'new user --> {email} \n'
          f'senha --> {senha}')

    senha_hash = generate_password_hash(senha)

    print(f'senha_hash --> {senha_hash} \n')

    button = request.form['name_submit']
    print(f'button --> {button} \n')

    if button == 'cadastrar':                   #botao cadastrar
        import sqlalchemy
        try:
            conn = engine.connect()
            conn.execute(f"insert into tb_users_vercel values (default, '{email}', '{senha_hash}')")
            print('')
            print('user adicionado c sucesso \n')
            return render_template('user_novo.html')
        except sqlalchemy.exc.IntegrityError:
            print('')
            print('esse user ja existe \n')
            return render_template('user_existe.html')

    elif button == 'login':                 #botao login
        conn = engine.connect()
        query_user = conn.execute(f"select email from tb_users_vercel where email = '{email}'")
        print('query_user --> ', query_user, '\n')
        for item in query_user:
            usuario = item.email
            print(usuario)

        try:
            if email == usuario:
                print('o email escrito no form consta no banco de dados')
                conn = engine.connect()
                query_senha = conn.execute(f"select * from tb_users_vercel where email = '{email}'")
                for item in query_senha:
                    query_senha = item.senha
                    print('query_senha -->', query_senha, '\n')
                query_senha = check_password_hash(query_senha, senha)
                if query_senha:
                    print('a senha informada pelo usuario esta de acordo com a senha do banco de dados')
                    #login_user(new_user)
                    return render_template('login_success.html')
                elif not query_senha:
                    print('a senha escrita no form n esta de acordo com a senha correspondente ao user escrito no form')
                    return render_template('senha_errada.html')
        except UnboundLocalError:
            print('o user escrito no form n consta no banco de dados')
            return render_template('login_fail.html')


@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
    try:
        id = id
        query = session.execute(text(f"select id, email from tb_users_vercel where id = {id}"))
        for item in query:
            email = item.email
        email = email
        return render_template('delete.html', id=id, email=email)
    except:
        return "this id dont have any user associated"


@app.route('/delete_user', methods=['GET', 'POST'])
def delete_user():
    id = request.form.get('name_email')
    try:
        conn = engine.connect()
        conn.execute(f"delete from tb_users_vercel where id = {id}")
        return render_template('user_deleted.html')
    except:                                             #usuario n achado, n existe, n tem oq deletar
        return render_template('user_deleted.html')


@app.errorhandler(404)
def error_404(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def error_500(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run(debug=True)

#isso aq so é p ter na branch teste