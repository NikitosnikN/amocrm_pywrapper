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


pipeline_step_colors = {
    'yellow': '#fff000',
    # fffeb2 	color example
    # fffd7f 	color example
    # fff000 	color example
    # ffeab2 	color example
    # ffdc7f 	color example
    # ffce5a 	color example
    # ffdbdb 	color example
    # ffc8c8 	color example
    # ff8f92 	color example
    # d6eaff 	color example
    # c1e0ff 	color example
    # 98cbff 	color example
    # ebffb1 	color example
    # deff81 	color example
    # 87f2c0 	color example
    # f9deff 	color example
    # f3beff 	color example
    # ccc8f9 	color example
    # eb93ff 	color example
    # f2f3f4 	color example
    # e6e8ea 	color example
}
