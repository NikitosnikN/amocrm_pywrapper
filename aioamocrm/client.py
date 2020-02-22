from .session import Session
from .models import *
from .managers import *

__all__ = ['AmoClient', ]


class AmoClient:
    session: Session = None
    account: Account = None
    leads: Lead = None
    pipelines: Pipeline = None
    companies: Company = None
    contacts: Contact = None
    customers: Customer = None
    tasks: Task = None
    notes: Note = None

    @classmethod
    def init(cls, login: str, token: str, subdomain: str):
        cls.session = Session.init(login, token, subdomain)
        cls.account = Account(manager=AccountManager(cls.session))
        cls.leads = Lead(manager=LeadManager(cls.session))
        cls.pipelines = Pipeline(manager=PipelineManager(cls.session))
        cls.companies = Company(manager=CompanyManager(cls.session))
        cls.contacts = Contact(manager=ContactManager(cls.session))
        cls.customers = Customer(manager=CustomerManager(cls.session))
        cls.tasks = Task(manager=TaskManager(cls.session))
        cls.notes = Note(manager=NoteManager(cls.session))
        return cls


