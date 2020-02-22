from typing import Union
from datetime import timedelta, datetime

from httpx import Client

from .exceptions import *

__all__ = ['Session', 'SESSION_LIFETIME']

SESSION_LIFETIME = timedelta(minutes=15)


class Session:
    _amo_login: str = None
    _amo_hash: str = None
    _subdomain: str = None
    _cookies: dict = None
    _cookies_last_update: datetime = None

    def __init__(self, amo_login: str, amo_hash: str, subdomain: str):
        self._amo_login = amo_login or self._amo_login
        self._amo_hash = amo_hash or self._amo_hash
        self._subdomain = subdomain or self._subdomain

    @classmethod
    def init(cls, amo_login: str, amo_hash: str, subdomain: str):
        cls._authorize(cls, amo_login, amo_hash, subdomain)
        return cls(amo_login, amo_hash, subdomain)

    @property
    def auth_url(self) -> str:
        return f"https://{self.subdomain}.amocrm.ru/private/api/auth.php"

    @property
    def api_url(self) -> str:
        return f"https://{self.subdomain}.amocrm.ru/api/v2/"

    @property
    def subdomain(self) -> str:
        return self._subdomain

    @property
    def cookies(self) -> Union[dict, None]:
        if self._cookies and self._cookies_last_update + SESSION_LIFETIME < datetime.now():
            return self._authorize()

        return self._cookies

    def _authorize(self, amo_login: str = None, amo_hash: str = None, subdomain: str = None) -> None:
        with Client() as session:
            resp = session.post(
                subdomain or self.auth_url,
                data={
                    'USER_LOGIN': amo_login or self._amo_login,
                    'USER_HASH': amo_hash or self._amo_hash,
                })

        if resp.status_code == 200 and 'true' in resp.text:
            self._cookies = dict(resp.cookies)
            self._cookies_last_update = datetime.now()
        else:
            raise AmoAuthError

    def request(self, method: str, url: str, payload: dict = None) -> Union[dict, None]:
        if payload:
            payload = {'params': payload} if method.lower() == 'get' else {'data': payload}
        else:
            payload = {}

        with Client() as session:
            resp = getattr(session, method)(url=url, **payload, cookies=self.cookies)

            if resp.status_code == 200:
                return resp.json()
            elif resp.status_code == 400:
                raise AmoBadRequest
            elif resp.status_code == 401:
                raise AmoAuthError
            elif resp.status_code == 402:
                raise AmoPaymentRequired
            elif resp.status_code == 403:
                raise AmoForbidden
            elif resp.status_code == 404:
                raise AmoPageNotFoundError
            elif resp.status_code == 500:
                raise AmoInternalError
            else:
                raise AmoUnknownError
