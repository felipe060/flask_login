from flask import Flask, render_template, request, redirect, url_for, request_finished, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, create_engine, text
from sqlalchemy.orm import declarative_base, sessionmaker
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

engine = create_engine('mysql+pymysql://root:eHr9fnsWdoa7lhIgcTd4@containers-us-west-176.railway.app/railway?6587', echo=True, query_cache_size=0,
                       connect_args=dict(host='containers-us-west-176.railway.app', port=6587))

Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:eHr9fnsWdoa7lhIgcTd4@containers-us-west-176.railway.app/railway?6587'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False        #default é True
app.config['SECRET_KEY'] = 'secret_key'

db = SQLAlchemy(app)


class User(Base):
    __tablename__ = 'tb_users_rail'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    user = Column(String(40), unique=True, nullable=False)
    senha = Column(String(240), nullable=False)

#Base.metadata.create_all(engine)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/add', methods=['GET', 'POST'])
def add_user():
    user = request.form.get('name_user')
    senha = request.form.get('name_senha')
    new_user = User(user=user, senha=senha)
    print('')
    print(f'funcao add_user \n \n'
          f'new user --> {user} \n'
          f'senha --> {senha} \n')
    import sqlalchemy
    try:
        conn = engine.connect()
        conn.execute(f"insert into tb_users_rail values (default, '{user}', '{senha}')")
        print('')
        print('user adicionado c sucesso \n')
        return render_template('user_novo.html')
    except sqlalchemy.exc.IntegrityError:
        print('')
        print('esse user ja existe \n')
        return render_template('user_existe.html')


@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
    try:
        id = id
        query =session.execute(text(f"select id, user from tb_users_rail where id = {id}"))
        for item in query:
            user = item.user
        user = user
        return render_template('delete.html', id=id, user=user)
    except:
        return "this id dont have any user associated"


@app.route('/delete_user', methods=['GET', 'POST'])
def delete_user():
    id = request.form.get('name_user')
    try:
        conn = engine.connect()
        conn.execute(f"delete from tb_users_rail where id = {id}")
        return render_template('user_deleted.html')
    except:
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