from usuario_dao import UsuarioDAO
from usuario import Usuario
from logger_base import log

print('Hola, ingresa un 2 si queres actualizar un registro de la tabla:')

num = int(input('Ingresa aca che: '))

if num == 2:
    id_var = int(input('Ingresa el id: '))
    username_var = input('Ingresa nuevo nombre: ')
    password_var = input('Ingresa la nueva contrasenha tambien: ')
    usuario = Usuario(id_var, username_var, password_var)
    aver = UsuarioDAO.actualizar(usuario)
    log.info(f'Usuario actualizado: {aver}')
