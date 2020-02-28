from traceback import format_stack, format_exc
import logging


class MakersiteException(Exception):

    _message = None
    _code = None
    _traceback = None
    _original_error = None

    def __init__(self, message, logmessage=None, code=500, logfn=logging.error):
        super(MakersiteException, self).__init__()
        self.traceback = format_exc(limit=None)
        self.stack = format_stack(limit=None)
        self.user_message = message
        self.code = code
        self.logmessage = logmessage or message
        self.logfn = logfn

    @property
    def exception(self):
        return self._original_error

    @exception.setter
    def exception(self, val):
        if not isinstance(val, Exception):
            self._original_error = "NOT A VALID ACCEPTION - " + str(val)
        else:
            self._original_error = val

    @property
    def traceback(self):
        return self._traceback

    @traceback.setter
    def traceback(self, val):
        self._traceback = val

    @property
    def user_message(self):
        return self._message

    @user_message.setter
    def user_message(self, val):
        if not (isinstance(val, str)):
            self._message = "NOT A VALID ERROR CODE - " + str(val)
        else:
            self._message = val

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, val):
        if not isinstance(val, int):
            self._code = "NOT A VALID CODE"
        else:
            self._code = val

    def log_and_message(self):
        if self.logfn:
            self.logfn(self.prepare_message_for_output())
        return ({"message": self.user_message}, self.code)

    def prepare_message_for_output(self):
        if self.logfn in [logging.error, logging.debug]:
            message = "----------\n".join(
                ["".join(self.stack[:-1]), self.traceback, self.logmessage]
            )
        else:
            message = self.logmessage
        return message


def catch_all_exceptions(f):
    def catch_exceptions(*args, **kwargs):
        try:
            res = f(*args, **kwargs)
        except MakersiteException as me:
            return me.log_and_message()
        except Exception as e:
            logging.error(
                "Caught error {e} with traceback {t}".format(e=str(e), t=format_exc())
            )
            return {"message": "An unknown error occurred"}, 500
        return res

    return catch_exceptions
