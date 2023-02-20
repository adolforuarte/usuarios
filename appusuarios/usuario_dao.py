from conexion import Conexion
from cursor_del_pool import CursorDelPool
from usuario import Usuario
from logger_base import log

class UsuarioDAO:

    _SELECCIONAR = 'SELECT * FROM usuarios ORDER BY id'
    _INSERTAR = 'INSERT INTO usuarios (username, password) VALUES (%s, %s)'
    _ACTUALIZAR = 'UPDATE usuarios SET username = %s, password = %s, id = %s'
    _ELIMINAR = 'DELETE FROM usuarios WHERE id = %s'

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            usuarios = []
            for registro in registros:
                usuario = Usuario(registro[0], registro[1], registro[2])
                usuarios.append(usuario)
            return usuarios

    @classmethod
    def insertar(cls, usuario):
        with CursorDelPool() as cursor:
            valores = (usuario.username, usuario.password)
            cursor.execute(cls._INSERTAR, valores)
            log.info(f'Usuario insertado: {usuario}')
            return cursor.rowcount

    @classmethod
    def actualizar(cls, usuario):
        with CursorDelPool() as cursor:
            valores = (usuario.username, usuario.password, usuario.id)
            cursor.execute(cls._ACTUALIZAR, valores)
            log.info(f'Usuario insertado: {usuario}')
            return cursor.rowcount

    @classmethod
    def eliminar(cls, usuario):
        with CursorDelPool() as cursor:
            valores = (usuario.id,)
            cursor.execute(cls._ELIMINAR, valores)
            log.info(f'Usuario insertado: {usuario}')
            return cursor.rowcount