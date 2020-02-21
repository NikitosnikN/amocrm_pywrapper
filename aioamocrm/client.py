from .session import Session
from .models import *


class Client:
    session: Session = None
    account: Account = None
    leads: Lead = None
    contacts: Contact = None
    pipelines: Pipeline = None

    @classmethod
    def init(cls, login: str, token: str, subdomain: str):
        cls.session = Session.init(login, token, subdomain)
        cls.account = Account(cls.session)
        cls.pipelines = Pipeline(cls.session)
        return cls


