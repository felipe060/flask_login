'''from werkzeug.security import generate_password_hash, check_password_hash

senha = 'melissa'

variavel = generate_password_hash(senha)

print(variavel)

#check_password_hash(hash_string, normal_string)
check = check_password_hash(variavel, senha)

print(check)


from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+pymysql://root:felipe008@localhost/flask_zero', echo=True)

Session = sessionmaker(bind=engine)
session = Session()

query = session.execute(text('select count(id) from tb_users where email like "e%"'))
#conn = engine.connect(close_with_result=True)


def funcao():
    conn = engine.connect()
    result = conn.execute(text("select count(id) from tb_users where email like 'e%' "))
    conn.close()
    for item in result:
        print(item)


#funcao()


def cadastro():
    entrada = input(str('digite uma palavra'))
    string_hash = generate_password_hash(entrada)
    print(string_hash)

    verifica = check_password_hash(string_hash, entrada)

    if verifica:
        print('a senha condiz c o hash')
    else:
        print('a senha n condiz c o hash')


#cadastro()


def verifica():
    usuario = 'celso@hotmail.com'
    conn = engine.connect()
    query = conn.execute(f"select * from tb_users where email = '{usuario}'")
    for item in query:
        user = item.email

    try:
        if usuario == user:
            query = True
            return query
    except UnboundLocalError:
        query = False
        return query


variave = verifica()
print(variave)

engine2 = create_engine('mysql+pymysql://root:felipe008@localhost/flask_zero')

conn2 = engine2.connect()
query2 = conn2.execute('select * from tb_posts2')

for item in query2:
    data = item.data
    print(item)'''



'''class Square:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        area = self.width * self.length
        return area


variavel = Square(20, 10)
print(variavel.area())
print('')


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def dados(self):
        print('name -->', self.name)
        print('age -->', self.age)
        return self.name, self.age

    def __str__(self):
        return f'name --> {self.name}\n' \
               f'age --> {self.age}'


p1 = Person('Melissa', 19)
print(p1)
print('-------------')
print(p1.name)
print(p1.age)
p1.dados()
print('----------')
print(p1.dados())
print('---------\n')

p1.age = 20
print(p1)
print('--------------')
p1.cor = 'branca'
print(p1.cor)
#del p1.cor
#print(p1.cor)'''



'''from flask import Flask, render_template
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy


app = Flask('teste')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:XYwWDEPmb53sQD3ezUeH@containers-us-west-35.railway.app/railway?6471'
#login_manager = LoginManager(app)
db = SQLAlchemy(app)


@app.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')


app.run(debug=True)'''


import MySQLdb
connection = MySQLdb.connect(
  host="aws.connect.psdb.cloud",
  user="gctqalwc42mndry0j5bf",
  passwd="pscale_pw_7WnPVnneTNaGjZYk5NnRHycEg6BPbS6iC4xUCohugue",
  db="flask_planet",
  autocommit=True,
  #ssl_mode="VERIFY_IDENTITY",
  ssl={'print': print('executando ssl'), "ca": "cacert-2023-08-22.pem", 'print2': print('ssl executado')}
)
print('tudo certo')


from sqlalchemy import create_engine, text
engine = create_engine('mysql+pymysql://gctqalwc42mndry0j5bf:pscale_pw_7WnPVnneTNaGjZYk5NnRHycEg6BPbS6iC4xUCohugue@aws.connect.psdb.cloud/flask_planet?ssl={"rejectUnauthorized":True}', echo=True, query_cache_size=0,
                       connect_args=dict(host='aws.connect.psdb.cloud', ssl={"ca": "cacert-2023-08-22.pem"}))
print('tudo certo 2')


conn = engine.connect()
query = conn.execute(text('select * from tb_users_planet'))

for item in query:
  print(item)
