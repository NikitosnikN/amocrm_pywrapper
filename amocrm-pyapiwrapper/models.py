from typing import List
from datetime import datetime

from .base import BaseModel
from .mixins import DateTimeModelMixin, ElementModelMixin, ColorMixin

__all__ = ['Account', 'Lead', 'Contact', 'Company', 'Customer', 'Task', 'Note', 'Pipeline']


class Account(BaseModel):
    _subdomain: str = None
    _currency: str = None
    _timezone: str = None
    _language: str = None
    _current_user: int = None
    _pipelines: list = None
    _users: list = None
    _groups: list = None
    _note_types: list = None
    _task_types: list = None


class Company(BaseModel, DateTimeModelMixin):
    _responsible_user_id: int = None
    _created_by: int = None
    _tags: str = None
    _leads_id: list = None
    _customers_id: str = None
    _contacts_id: list = None


class Contact(BaseModel, DateTimeModelMixin):
    _responsible_user_id: int = None
    _created_by: int = None
    _tags: str = None
    _leads_id: list = None
    _company_id: int = None


class Status(BaseModel, ColorMixin):
    _sort: int = None
    _is_editable: bool = None

    def __init__(self, *, manager=None, **kwargs):
        super().__init__(manager=manager)
        self.__parse_from__(**kwargs)

    def __repr__(self):
        return f"Status '{self.name}'"

    def __parse_from__(self, **kwargs):
        for key, val in kwargs.items():
            setattr(self, f'_{key}', val) if hasattr(self, f'_{key}') else None

    @property
    def color(self):
        return f"Yellow ({self._color})"


class Pipeline(BaseModel):
    _sort: int = None
    _is_main: bool = None
    _statuses: list = None

    def __init__(self, *, manager=None, **kwargs):
        super().__init__(manager=manager)
        self.__parse_from__(**kwargs)

    def __repr__(self):
        return f"Pipeline '{self.name}'"

    def __parse_from__(self, **kwargs):
        for key, val in kwargs.items():
            if key == 'statuses':
                self._statuses.extend([Status(**status) for status in val.values()])
            else:
                setattr(self, f'_{key}', val) if hasattr(self, f'_{key}') else None

    @property
    def statuses(self):
        if isinstance(self._statuses, dict):
            return [Status(**status) for status in self._statuses]
        else:
            return self._statuses


class Lead(BaseModel, DateTimeModelMixin):
    _responsible_user_id: int = None
    _created_by: int = None
    _account_id: int = None
    _is_deleted: bool = None
    _main_contact: Contact = None
    _group_id: int = None
    _company: Company = None
    _closed_at: datetime = None
    _closest_task_at: datetime = None
    _tags: list = None
    _contacts: List[Contact] = None
    _status_id: int = None
    _pipeline_id: int = None
    _sale: int = None

    def __init__(self, *, manager=None, **kwargs):
        super().__init__(manager=manager)
        self.__parse_from__(**kwargs)

    def __repr__(self):
        return f"Lead '{self.name}'"

    def __parse_from__(self, **kwargs):
        for key, val in kwargs.items():
            if key == 'custom_fields':
                pass
            elif key in ('main_contact', 'contacts'):
                pass
            elif key in ('created_at', 'updated_at', 'closest_task_at') and isinstance(val, str):
                setattr(self, f'_{key}', datetime.fromisoformat(val))
            else:
                setattr(self, f'_{key}', val) if hasattr(self, f'_{key}') else None


class Customer(BaseModel):
    _responsible_user_id: int = None
    _created_by: int = None
    _next_date: datetime = None
    _next_price: int = None
    _periodicity: int = None
    _contacts_id: list = None
    _company_id: int = None
    _tags: list = None
    _period_id: int = None
    _catalog_elements_id: dict = None


class Task(BaseModel, DateTimeModelMixin, ElementModelMixin):
    _responsible_user_id: int = None
    _created_by: int = None
    _complete_till_at: datetime = None
    _task_type: int = None
    _text: str = None


class Note(BaseModel):
    _note_type: int = None
    _responsible_user_id: int = None
    _created_by: int = None
    _params: list = None
    _text: str = None
