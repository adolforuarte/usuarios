from logger_base import log

class Persona:
    def __init__(self, id = None, nombre = None, apellido = None, email = None):
        self._id = id
        self._nombre = nombre
        self._apellido = apellido
        self._email = email

    def __str__(self):
        return f'''
            ID: {self._id},
            NOMBRE: {self._nombre},
            APELLIDO: {self._apellido},
            EMAIL: {self._email}
        '''

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email

if __name__ == '__main__':
    persona1 = Persona(1, 'Juan', 'Perez', 'jperez@mail.com')
    log.debug(persona1)
    persona2 = Persona(nombre = 'Mauro', apellido = 'Diaz', email = 'mdiaz@mail.com')
    log.debug(persona2)









