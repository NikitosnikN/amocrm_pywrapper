from types import Union

from .utils import get_embedded_items

BASE_API_URL = 'https://{}.amocrm.ru/api/v2/{}'


class _BaseModel(object):
    _id: int = None
    _name: str = None
    _href: str = None


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
