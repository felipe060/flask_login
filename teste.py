from werkzeug.security import generate_password_hash, check_password_hash

senha = 'melissa'

variavel = generate_password_hash(senha)

print(variavel)


