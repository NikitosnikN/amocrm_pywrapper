from typing import Optional, Union
from datetime import timedelta, datetime

from httpx import Client

from .exceptions import AmoAuthError, AmoPageNotFoundError, AmoInternalError, AmoBadRequest

SESSION_LIFETIME = timedelta(minutes=15)


class Session:
    _amo_login: str = None
    _amo_hash: str = None
    _subdomain: str = None
    _cookies = None
    _cookies_last_update: datetime = None

    def __init__(self, amo_login: str, amo_hash: str, subdomain: str):
        self._amo_login = amo_login or self._amo_login
        self._amo_hash = amo_hash or self._amo_hash
        self._subdomain = subdomain or self._subdomain

    @classmethod
    def init(cls, amo_login: str, amo_hash: str, subdomain: str):
        cls._get_cookies(cls, amo_login, amo_hash, subdomain)
        return cls(amo_login, amo_hash, subdomain)

    @property
    def subdomain(self) -> str:
        return self._subdomain

    @property
    def cookies(self) -> Union[dict, None]:
        if self._cookies and self._cookies_last_update + SESSION_LIFETIME < datetime.now():
            return self._get_cookies(self._amo_login, self._amo_hash, self._subdomain)

        return self._cookies

    def _get_cookies(self, amo_login: str, amo_hash: str, subdomain: str) -> None:

        url = f"https://{subdomain}.amocrm.ru/private/api/auth.php"
        payload = {
            'USER_LOGIN': amo_login,
            'USER_HASH': amo_hash,
        }
        with Client() as session:
            resp = session.post(url, data=payload)

        if resp.status_code == 200 and 'true' in resp.text:
            self._cookies = dict(resp.cookies)
            self._cookies_last_update = datetime.now()
        else:
            raise AmoAuthError

    def request(self, method: str, url: str, payload: dict = None, headers: dict = None) -> Union[dict, None]:
        header = {}
        if headers:
            header.update(**headers)

        if payload:
            payload = {'params': payload} if method.lower() == 'get' else {'json': payload}
        else:
            payload = {}

        with Client() as session:
            resp = getattr(session, method)(url=url, **payload, cookies=self.cookies)

            if resp.status_code == 200:
                return resp.json()
            elif resp.status_code == 401:
                raise AmoAuthError
            elif resp.status_code == 404:
                return None
            elif resp.status_code == 500:
                raise AmoInternalError
            else:
                raise AmoBadRequest
