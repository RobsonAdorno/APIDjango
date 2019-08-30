import os

print('Script para criar usuário iniciado...')

username = str(input('Digite o seu usuário'))
email = str(input('Digite o seu email, por favor'))

os.system('python3 manage.py createsuperuser --email {} --username {}'.format(email, username))

