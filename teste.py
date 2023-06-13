from werkzeug.security import generate_password_hash, check_password_hash

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
    print(item)

