from modules.getRabbitMQ import *
import sys, os


if __name__ == '__main__':
    try:
        getRabbit()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)

