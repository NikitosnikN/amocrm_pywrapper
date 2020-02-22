from datetime import datetime

__all__ = ['ElementModelMixin', 'DateTimeModelMixin', 'ColorMixin']


class ElementModelMixin(object):
    _element_id: int = None
    _element_type: int = None

    @staticmethod
    def element_type_dict() -> dict:
        return {
            1: 'Contact',
            2: 'Lead',
            3: 'Company',
            4: 'Task',
            12: 'Customer',
        }


class DateTimeModelMixin(object):
    _created_at: datetime = None
    _updated_at: datetime = None


class ColorMixin(object):
    _color: str = None

    @staticmethod
    def color_dict() -> dict:
        # TODO fill colors
        return {
            '#fffeb2': '#fffeb2',
            '#fffd7f': '#fffd7f',
            'yellow': '#fff000',
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
