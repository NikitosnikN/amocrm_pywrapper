__all__ = ['Account', 'Lead', 'Contact', 'Company', 'Customers', 'Tasks', 'Notes', 'Pipeline']

from typing import List, Dict
from datetime import datetime

from .base import _BaseModel
from .fields import CustomField


class Account(_BaseModel):
    _subdomain: str = None
    _currency: str = None
    _timezone: str = None
    _language: str = None
    _current_user: int = None
    _pipelines: list = None
    _users: list = None
    _custom_fields: list = None
    _groups: list = None
    _note_types: list = None
    _task_types: list = None


class Company(_BaseModel):
    pass


class Contact(_BaseModel):
    pass


class Status(_BaseModel):
    _color: str = None
    _sort: int = None
    is_editable: bool = None

    def __repr__(self):
        return f"Status '{self.name}'"

    def __parse_from(self, **kwargs):
        for key, val in kwargs.items():
            setattr(self, f'_{key}', val) if hasattr(self, f'_{key}') else None

    @property
    def color(self):
        return f"Yellow ({self._color})"


class Pipeline(_BaseModel):
    _sort: int = None
    _is_main: bool = None
    _statuses: list = list()

    def __repr__(self):
        return f"Pipeline '{self.name}'"

    def __parse_from(self, **kwargs):
        for key, val in kwargs.items():
            if key == 'statuses':
                self._statuses.extend([Status(**status) for status in val.values()])
            else:
                setattr(self, f'_{key}', val) if hasattr(self, f'_{key}') else None


class Lead(_BaseModel):
    _responsible_user_id: int = None
    _created_by: int = None
    _created_at: datetime = None
    _updated_at: datetime = None
    _account_id: int = None
    _is_deleted: bool = None
    _main_contact: Contact = None
    _group_id: int = None
    _company: Company = None
    _closed_at: int = None
    _closest_task_at: datetime = None
    _tags: list = None
    _custom_fields: List[CustomField] = None
    _contacts: List[Contact] = None
    _status_id: int = None
    _sale: int = None
    _pipeline: Pipeline = None

    def __init__(self, *, manager=None, **kwargs):
        super().__init__(manager=manager)

        self.__parse_from(**kwargs) if kwargs else None

    def __repr__(self):
        return f"Lead '{self.name}'"

    def __parse_from(self, **kwargs):
        for key, val in kwargs.items():
            if key == 'custom_fields':
                pass
            else:
                setattr(self, f'_{key}', val) if hasattr(self, f'_{key}') else None


class Customers(_BaseModel):
    pass


class Tasks(_BaseModel):
    pass


class Notes(_BaseModel):
    pass
