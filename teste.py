from werkzeug.security import generate_password_hash, check_password_hash

senha = 'melissa'

variavel = generate_password_hash(senha)

print(variavel)

#check_password_hash(hash_string, normal_string)
check = check_password_hash(variavel, senha)

print(check)
