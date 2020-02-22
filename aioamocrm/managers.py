import json
from typing import Union

from .base import BaseManager
from .models import *
from .utils import AmoJSONEncoder

__all__ = ['AccountManager', 'LeadManager', 'PipelineManager', 'CompanyManager', 'ContactManager', 'CustomerManager',
           'TaskManager', 'NoteManager']


class AccountManager(BaseManager):
    model_name = 'account'

    def fetch(self, payload: dict = None) -> dict:
        return self.session.request(
            method='get',
            url=self.api_url,
            payload=payload
        )


class LeadManager(BaseManager):
    model_name = 'leads'

    def fetch_all(self, payload: dict = None) -> Union[dict, None]:
        return super().fetch_all(payload)

    def add(self, leads: Union[Lead, dict, list] = None) -> dict:
        if isinstance(leads, dict):
            leads = Lead(**leads)

        payload = json.dumps(leads, cls=AmoJSONEncoder)

        return super().add(payload=payload)

    def update(self, leads: Union[Lead, dict, list] = None) -> dict:
        if isinstance(leads, dict):
            leads = Lead(**leads)

        payload = json.dumps(leads, cls=AmoJSONEncoder)

        return super().add(payload=payload)


class PipelineManager(BaseManager):
    model_name = 'pipelines'

    def fetch_all(self, payload: dict = None) -> Union[list, None]:
        objects = super().fetch_all(payload)
        return list(Pipeline(**obj) for obj in objects.values())


class StatusManager(BaseManager):
    model_name = 'pipelines'

    def fetch_all_from_pipeline(self, payload: dict = None) -> Union[dict, None]:
        pipeline = super().fetch_one(_id=payload.get('pipeline_id'))

        if not pipeline:
            return None

        pass


class ContactManager(BaseManager):
    model_name = 'contacts'

    def fetch_all(self, payload: dict = None) -> Union[dict, None]:
        return super().fetch_all(payload)


class CompanyManager(BaseManager):
    model_name = 'companies'

    def fetch_all(self, payload: dict = None) -> Union[dict, None]:
        return super().fetch_all(payload)


class CustomerManager(BaseManager):
    model_name = 'customers'

    def fetch_all(self, payload: dict = None) -> Union[dict, None]:
        return super().fetch_all(payload)


class TaskManager(BaseManager):
    model_name = 'tasks'

    def fetch_all(self, payload: dict = None) -> Union[dict, None]:
        return super().fetch_all(payload)


class NoteManager(BaseManager):
    model_name = 'notes'

    def fetch_all(self, payload: dict = None) -> Union[dict, None]:
        return super().fetch_all(payload)


class FieldManager(BaseManager):
    model_name = 'fields'

    def fetch_all(self, payload: dict = None): return None

    def fetch_one(self, _id: int): return None
