# -*- coding: utf-8 -*-

# std
import os.path

# tango
from tango.core import WSGIApplication
from tango.utils.wsgi import WSGIValidator


application = WSGIValidator(WSGIApplication(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'sgservice')))

if __name__ == '__main__':
    # в случае запуска через встроенный WSGI
    # сервер добавляем вывод сообщений на консоль
    from tango import logger
    logger.add_console()

    # подготавливаем и запускаем встроенный
    # WSGI сервер
    from tango.utils.wsgi import WSGIServer
    server = WSGIServer(application)
    server.run()