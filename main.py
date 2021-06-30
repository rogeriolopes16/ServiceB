from modules.getRabbitMQ import *
import sys, os


if __name__ == '__main__':
    try:
        getRabbit() # chama funtion do serviço que pega informações no RabbitMQ e envia para S3
    except KeyboardInterrupt:
        # caso exista exceção o serviço é encerrado.
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)

