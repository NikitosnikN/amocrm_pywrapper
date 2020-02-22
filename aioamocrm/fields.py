from typing import List, Union

from .base import _BaseField


class TextField(_BaseField):
    _type: int = 1


class NumericField(_BaseField):
    _type: int = 2


class CheckBoxField(_BaseField):
    _type: int = 3


class SelectField(_BaseField):
    _type: int = 4
    _enum: List[str] = None


class MultiSelectField(_BaseField):
    _type: int = 5
    _enum: List[str] = None


class DateField(_BaseField):
    _type: int = 6


class UrlField(_BaseField):
    _type: int = 7


class MultiTextField(_BaseField):
    _type: int = 8


class TextAreaField(_BaseField):
    _type: int = 9


class RadioButtonField(_BaseField):
    _type: int = 10


class StreetAddressField(_BaseField):
    _type: int = 11


class SmartAddressField(_BaseField):
    _type: int = 12


class BirthdayField(_BaseField):
    _type: int = 13


class LegalEntityField(_BaseField):
    _type: int = 14


class ItemsField(_BaseField):
    _type: int = 15


class CustomField(_BaseField):
    _values: Union[list, int, str] = None
    _enum: List[str] = None

