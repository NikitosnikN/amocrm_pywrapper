__all__ = ['AccountManager', 'LeadManager', 'PipelineManager', 'CompanyManager', 'ContactManager', 'CustomersManager',
           'TasksManager', 'NotesManager']

from typing import Union
import json
from pprint import pprint

from .base import _BaseManager
from .models import *
from .utils import get_embedded_items, AmoJSONEncoder


class AccountManager(_BaseManager):
    model_name = 'account'

    def fetch(self, payload: dict = None) -> dict:
        return self.session.request(
            method='get',
            url=self.api_url,
            payload=payload
        )


class LeadManager(_BaseManager):
    model_name = 'leads'

    def fetch_all(self, payload: dict = None) -> Union[dict, None]:
        return super().fetch_all(payload)
    
    def add(self, leads: Union[Lead, dict, list] = None) -> dict:
        if isinstance(leads, dict):
            leads = Lead(**leads)

        if not isinstance(leads, list):
            leads = [leads, ]

        payload = json.dumps(leads, cls=AmoJSONEncoder)

        return super().add({'add': payload})

    def update(self, leads: Union[Lead, dict, list] = None) -> dict:
        if isinstance(leads, dict):
            leads = Lead(**leads)

        if not isinstance(leads, list):
            leads = [leads, ]

        payload = json.dumps(leads, cls=AmoJSONEncoder)

        return super().add({'add': payload})


class PipelineManager(_BaseManager):
    model_name = 'pipelines'

    def fetch_all(self, payload: dict = None) -> Union[list, None]:
        objects = super().fetch_all(payload)
        # pprint(objects)
        return list(Pipeline(**obj) for obj in objects.values())


class StatusManager(_BaseManager):
    model_name = 'pipelines'

    def fetch_all_from_pipeline(self, payload: dict = None) -> Union[dict, None]:
        pipeline = super().fetch_one(_id=payload.get('pipeline_id'))

        if not pipeline:
            return None

        pass


class ContactManager(_BaseManager):
    model_name = 'contacts'

    def fetch_all(self, payload: dict = None) -> Union[dict, None]:
        return super().fetch_all(payload)


class CompanyManager(_BaseManager):
    model_name = 'companies'

    def fetch_all(self, payload: dict = None) -> Union[dict, None]:
        return super().fetch_all(payload)


class CustomersManager(_BaseManager):
    model_name = 'customers'

    def fetch_all(self, payload: dict = None) -> Union[dict, None]:
        return super().fetch_all(payload)


class TasksManager(_BaseManager):
    model_name = 'tasks'

    def fetch_all(self, payload: dict = None) -> Union[dict, None]:
        return super().fetch_all(payload)


class NotesManager(_BaseManager):
    model_name = 'notes'

    def fetch_all(self, payload: dict = None) -> Union[dict, None]:
        return super().fetch_all(payload)


class FieldManager(_BaseManager):
    model_name = 'fields'

    def add(self):
        pass

    def delete(self):
        pass

    def fetch_all(self, payload: dict = None) -> Union[dict, None]:
        return None

    def fetch_one(self, _id: int) -> Union[dict, None]:
        return None