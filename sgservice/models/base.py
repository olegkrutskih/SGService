# -*- coding: utf-8 -*-

# tango
from tango.utils.inspect import class_name


class ModelError(Exception):
    """
    Класс для обозначения ошибок, которые возникли при
    работе с моделью данных (нет прав, нет пользователя, ...).
    """
    def __init__(self, message):
        from tango.utils.converts import to_string
        Exception.__init__(self, to_string(message, encoding='utf-8'))


class ModelInterfaceError(ModelError):
    """
    Класс для обозначения ошибок, которые возникли при
    работе с интерфейсом, предоставляющим доступ к данным
    через различные механизмы.
    """
    def __init__(self, message):
        ModelError.__init__(self, message)


class ModelBase(object):
    def get_rights(self, user):
        """
        Возвращает словарь прав для пользователя,его id и ФИО в виде
        tuple объекта (id_user, name, rights).
        <user> - имя пользователя (логин/alias)
        """
        raise NotImplementedError('%s.get_rights' % class_name(self))

    def get_builds(self, id_user):
        """
        Возвращает список зданий.
        <id_user> - ID пользователя
        """
        raise NotImplementedError('%s.get_builds' % class_name(self))

