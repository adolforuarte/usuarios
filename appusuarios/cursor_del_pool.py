from conexion import Conexion
from logger_base import log

class CursorDelPool:
    def __init__(self):
        self._conexion = None
        self._cursor = None

    def __enter__(self):
        self._conexion = Conexion.obtenerConexion()
        self._cursor = self._conexion.cursor()
        return self._cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_val:
            self._conexion.rollback()
            log.error(f'Ocurrio una excepcion, rollback: {exc_val} - {exc_type} - {exc_tb}')
        else:
            self._conexion.commit()
        self._cursor.close()
        Conexion.liberarConexion(self._conexion)
'''
if __name__ == '__main__':
    with CursorDelPool() as cursor:
        log.debug('Dentro del bloque with.')
        cursor.execute('SELECT * FROM usuarios')
        log.debug(cursor.fetchall())
'''
