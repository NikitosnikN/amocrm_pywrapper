from typing import Union, Any

from .mixins import ElementModelMixin
from .utils import get_embedded_items


class BaseModel(object):
    _id: int = None
    _name: str = None
    _href: str = None
    _custom_fields: list = None

    objects = NotImplemented

    def __init__(self, *, manager=None, **kwargs):
        self.objects = manager if manager else NotImplemented
        self.__parse_from__(**kwargs) if kwargs else None

    def __repr__(self):
        return self.__class__.__name__

    def __parse_from__(self, **kwargs):
        for key, val in kwargs.items():
            setattr(self, f'_{key}', val) if hasattr(self, f'_{key}') else None

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def href(self):
        return self._href


class BaseManager(object):
    model_name: str = None
    custom_api_url: str = None
    session = None

    def __init__(self, session):
        self.session = session

    @property
    def api_url(self) -> str:
        endpoint = self.custom_api_url or self.model_name
        return self.session.api_url + endpoint

    def fetch_one(self, _id: int) -> Union[dict, None]:
        return self.session.request(
            method='get',
            url=self.api_url,
            payload={'id': _id}
        )

    def fetch_all(self, payload: dict = None) -> Union[dict, None]:
        return get_embedded_items(
            self.session.request(
                method='get',
                url=self.api_url,
                payload=payload
            )
        )

    def fetch_related(self, url: str, payload: dict) -> Union[dict, None]:
        return self.session.request(
            method='get',
            url=url,
            payload=payload
        )

    def add(self, payload: Any = None):
        return self.session.request(
            method='post',
            url=self.api_url,
            payload={
                'add': payload if isinstance(payload, (list, tuple, set)) else [payload, ]
            }
        )

    def update(self, payload: Any = None):
        return self.session.request(
            method='post',
            url=self.api_url,
            payload={
                'update': payload if isinstance(payload, (list, tuple, set)) else [payload, ]
            }
        )

    def delete(self, payload: Any = None):
        return self.session.request(
            method='post',
            url=self.api_url,
            payload={
                'delete': payload if isinstance(payload, (list, tuple, set)) else [payload, ]
            }
        )


class _BaseField(BaseModel, ElementModelMixin):
    _type: int = None
    _origin: str = None
    _is_editable: bool = None
    _is_required: bool = None
    _is_deletable: bool = None
    _is_visible: bool = None

    def __init__(self, *, manager=None, **kwargs):
        super().__init__(manager=manager)
        self.__parse_from__(**kwargs)

    def __repr__(self):
        return f"{self.__class__.__name__} '{self._name}'"

    def __parse_from__(self, **kwargs):
        for key, val in kwargs.items():
            if key == 'type':
                continue

            setattr(self, f'_{key}', val) if hasattr(self, f'_{key}') else None

        return None


class _BaseException(Exception):
    message = None

    def __init__(self, message=None):
        self.message = message or self.message
        super().__init__(self.message)

    def __str__(self):
        return self.message
