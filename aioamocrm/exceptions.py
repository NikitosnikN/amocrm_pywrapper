from .base import _BaseException

__all__ = ['AmoAuthError', 'AmoPageNotFoundError', 'AmoInternalError', 'AmoObjectNotFoundError', 'AmoBadRequest',
           'AmoUnknownError', 'AmoPaymentRequired', 'AmoForbidden']


class AmoAuthError(_BaseException):
    message = '№401. Invalid credentials or account has no permissions'


class AmoPaymentRequired(_BaseException):
    message = '№402. Payment Required'


class AmoForbidden(_BaseException):
    message = '№403. IP was banned or account was blocked'


class AmoPageNotFoundError(_BaseException):
    message = '№404. Page not found'


class AmoInternalError(_BaseException):
    message = '№500. AmoCRM Internal Error'


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


class AmoUnknownError(_BaseException):
    message = 'Unknown Error'
