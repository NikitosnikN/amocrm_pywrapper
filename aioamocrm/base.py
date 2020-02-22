from typing import Union

from .utils import get_embedded_items

BASE_API_URL = 'https://{}.amocrm.ru/api/v2/{}'


class BaseModel(object):
    _id: int = None
    _name: str = None
    _href: str = None

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


class _BaseManager(object):
    api_url: str = None
    model_name: str = None
    session = None

    def __init__(self, session):
        self.session = session
        self.api_url = BASE_API_URL.format(session.subdomain, self.model_name)

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

    def set(self):
        pass

    def add(self, payload: dict = None):
        return self.session.request(
            method='post',
            url=self.api_url,
            payload=payload
        )

    def delete(self, payload: dict = None):
        return self.session.request(
            method='delete',
            url=self.api_url,
            payload=payload
        )


class _BaseField(BaseModel):
    _type: int = None
    _origin: str = None
    _element_type: int = None
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
