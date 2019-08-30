import os

name_modulo = str(input('Digite o nome do modulo\n'))

if name_modulo:
    os.system('python3 manage.py startapp {}'.format(name_modulo))
    print('Modulo {} criado com sucesso!'.format(name_modulo))
else:
    print('Cara, não posso criar um modulo nulo!')