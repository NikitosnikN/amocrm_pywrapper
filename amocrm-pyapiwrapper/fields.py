from typing import List, Union

from .base import BaseField

__all__ = ['TextField', 'NumericField', 'CheckBoxField', 'SelectField', 'MultiSelectField', 'DateField', 'UrlField',
           'MultiTextField', 'TextAreaField', 'RadioButtonField', 'StreetAddressField', 'SmartAddressField', 
           'BirthdayField', 'LegalEntityField', 'ItemsField', 'CustomField']


class TextField(BaseField):
    _type: int = 1


class NumericField(BaseField):
    _type: int = 2


class CheckBoxField(BaseField):
    _type: int = 3


class SelectField(BaseField):
    _type: int = 4
    _enum: List[str] = None


class MultiSelectField(BaseField):
    _type: int = 5
    _enum: List[str] = None


class DateField(BaseField):
    _type: int = 6


class UrlField(BaseField):
    _type: int = 7


class MultiTextField(BaseField):
    _type: int = 8


class TextAreaField(BaseField):
    _type: int = 9


class RadioButtonField(BaseField):
    _type: int = 10


class StreetAddressField(BaseField):
    _type: int = 11


class SmartAddressField(BaseField):
    _type: int = 12


class BirthdayField(BaseField):
    _type: int = 13


class LegalEntityField(BaseField):
    _type: int = 14


class ItemsField(BaseField):
    _type: int = 15


class CustomField(BaseField):
    _values: Union[list, int, str] = None
    _enum: List[str] = None

