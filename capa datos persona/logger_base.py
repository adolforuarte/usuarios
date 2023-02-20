import logging as log

log.basicConfig(level = log.DEBUG,
                format = '%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',
                #hasta aca el formato que manejamos a la consola
                datefmt = '%I:%M:%S %p', #modifica la forma en que se muestra la fecha
                handlers = [#no solo enviara infor a consola, tambien a un archivo
                    log.FileHandler('capa_datos.log'),
                    log.StreamHandler()#basicamente, la consola que se ha manejado hasta el momento
                ])

#(asctime)agrega el tiempo(fechay hora) al mensaje del log
#(levelname)agrega si fue debug, info, warning, error o critical
#(filename)agrega el nombre del archivo al mensaje de log
#(lineno)agrega el numero de linea al mensaje de log
#(message)muestra el mensaje que se agrego al log

if __name__ == '__main__':
    log.debug('Mensaje a nivel debug.')
    log.info('Mensaje a nivel info.')
    log.warning('Mensaje a nivel warning.')
    log.error('Mensaje a nivel error.')
    log.critical('Mensaje a nivel critial.')
