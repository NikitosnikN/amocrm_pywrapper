from typing import Union

from .utils import get_embedded_items, raise_

BASE_API_URL = 'https://{}.amocrm.ru/api/v2/{}'


class _BaseModel(object):
    _id: int = None
    _name: str = None
    _href: str = None

    objects = NotImplemented

    def __init__(self, *, manager, **kwargs):
        self.objects = manager if manager else NotImplemented
        self.__parse_from(**kwargs) if kwargs else None

    def __repr__(self):
        return self.__class__.__name__

    def __parse_from(self, **kwargs):
        raise NotImplementedError('__parse_from should be implemented')

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def href(self):
        return self._href

    def to_json(self):
        return {
            attr[1:]: getattr(self, attr)
            for attr in [i for i in dir(self) if i[0] == '_' and not i[1] == '_' and not callable(i)]
        }


class _BaseField(object):
    pass


class _BaseManager(object):
    api_url: str = None
    model_name: str = None
    session = None

    def __init__(self, session):
        self.session = session
        self.api_url = BASE_API_URL.format(session.subdomain, self.model_name)

    def fetch_all(self, payload: dict = None) -> Union[dict, None]:
        return get_embedded_items(
            self.session.request(
                method='get',
                url=self.api_url,
                payload=payload
            )
        )


class _BaseException(Exception):
    message = None

    def __init__(self, message=None):
        self.message = message or self.message
        super().__init__(self.message)

    def __str__(self):
        return self.message
