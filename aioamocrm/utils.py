__all__ = ['AmoJSONEncoder', 'get_embedded_items']

from typing import Union
from json import JSONEncoder


# TODO improve class serialization
class AmoJSONEncoder(JSONEncoder):
    def default(self, o):
        return {
            attr[1:]: getattr(o, attr)
            for attr
            in [i for i in dir(o) if i[0] == '_' and not i[1] == '_' and not callable(i)]
            if getattr(o, attr) is not None
        }


def get_embedded_items(payload: dict) -> Union[dict, None]:
    return payload['_embedded']['items'] \
        if payload.get('_embedded') and payload['_embedded'].get('items') \
        else None
