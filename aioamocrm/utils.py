from typing import Union, DefaultDict


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
