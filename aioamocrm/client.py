from .session import Session
from .models import *
from .managers import *


class Client:
    session: Session = None
    account: Account = None
    leads: Lead = None
    contacts: Contact = None
    pipelines: Pipeline = None

    @classmethod
    def init(cls, login: str, token: str, subdomain: str):
        cls.session = Session.init(login, token, subdomain)
        cls.account = Account(manager=AccountManager(cls.session))
        cls.pipelines = Pipeline(manager=PipelineManager(cls.session))
        return cls


