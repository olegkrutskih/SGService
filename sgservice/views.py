# -*- coding: utf-8 -*-

# tango
import tango
import tango.db
from tango.publisher.jsonrpc import JsonRpcPublisher, JRPC_ERROR

# project
from common.constants import *
from models.base import *
import json


class JsonRpcService(JsonRpcPublisher):

    def __call_jrpc__(self, context, handler, args, kwargs):
        try:
            return JsonRpcPublisher.__call_jrpc__(self, context, handler, args, kwargs)
        except ModelInterfaceError, e:
            # ошибки интерфейса пользователю не отображаем
            tango.logger.error(e.message)
            raise JRPC_ERROR(u'Ошибка при работе с данными')
        except ModelError, e:
            # ошибки модели данных можно показывать пользователю
            tango.logger.error(e.message)
            raise JRPC_ERROR(e.message)

    def get_order(self, context, args):
        id_order = args.get('order_id')

        if (id_order is None) | (isinstance(id_order, int) is False):
            wrong_order = json.loads(answer_template)
            wrong_order["error"] = error_order_tpl
            return wrong_order

        answer = json.loads(answer_template)
        if id_order == -1:
            answer["data"] = json.loads(error_data_tpl)
            return answer
        else:
            answer["data"] = json.loads(valid_data_tpl)
            return answer
