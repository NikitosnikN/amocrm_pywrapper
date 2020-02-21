__all__ = ['AmoAuthError', 'AmoPageNotFoundError', 'AmoInternalError', 'AmoObjectNotFoundError', 'AmoBadRequest']

from .base import _BaseException


class AmoAuthError(_BaseException):
    message = 'Invalid credentials'


class AmoPageNotFoundError(_BaseException):
    message = '404. Page not found'


class AmoInternalError(_BaseException):
    message = '500. AmoCRM Internal Error'


class AmoObjectNotFoundError(_BaseException):
    message = 'Object not found'


class AmoBadRequest(_BaseException):
    message = 'Bad request'


class AmoBadResponse(_BaseException):
    message = 'Bad response'


class AmoWrapperHasNoPermission(_BaseException):
    pass


class AmoClientHasNoPermission(_BaseException):
    pass