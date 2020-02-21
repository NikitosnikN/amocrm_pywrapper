__all__ = ['AccountManager', 'LeadManager', 'PipelineManager', 'CompanyManager', 'ContactManager', 'CustomersManager',
           'TasksManager', 'NotesManager']

from typing import Union

from .base import _BaseManager
from .utils import get_embedded_items


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
    
    def add(self, payload: dict = None) -> dict:
        return self.session.request(
            method='post',
            url=self.api_url,
            payload={
                'add': payload
            }
        )

    def update(self, payload: dict = None) -> dict:
        return self.session.request(
            method='post',
            url=self.api_url,
            payload={
                'update': payload
            }
        )


class PipelineManager(_BaseManager):
    model_name = 'pipelines'

    def fetch_one(self, _id: int) -> Union[dict, None]:
        return self.session.request(
            method='get',
            url=self.api_url,
            payload={'id': _id}
        )

    def fetch_all(self, payload: dict = None) -> Union[dict, None]:
        return super().fetch_all(payload)
            
    def set(self, payload):
        pass

    def delete(self, _id):
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