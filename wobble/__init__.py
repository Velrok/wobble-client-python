# -*- coding: utf-8 -*-
import logging
import jsonrpclib


class LoginRequiredException(Exception):
    pass


def log_calls(fn):
    def log_calls_decorator(*args, **kwargs):
        self = args[0]
        params = args[1:]

        logging.debug("{obj}.{method}{args}".format(
            obj=self, method=fn.func_name, args=params))

        result = fn(*args, **kwargs)

        logging.debug("{obj}.{method}{args} ->\t{result}".format(
            obj=self, method=fn.func_name, args=params, result=result))

        return result

    return log_calls_decorator


def api_key_injector(fn, api_key):
    def inject_api_key(*args, **kwargs):
        # inject the apikeys
        kwargs['apikey'] = api_key

        return fn(*args, **kwargs)

    return inject_api_key


class WobbleService(object):
    """WobbleService"""

    def __init__(self, api_endpoint='http://wobble.moinz.de/api/endpoint.php',
                 json_rpc_server_class=jsonrpclib.Server):
        super(WobbleService, self).__init__()
        self.wobble_server = json_rpc_server_class(api_endpoint)
        self.api_endpoint = api_endpoint
        self.api_key = None
        self.last_notification_timestamp = None
        self.logger = None

    def __enter__(self):
        return self

    def __exit__(self, exception=None, error=None, traceback=None):
        self.user_signout()
        if exception:
            raise exception, error, traceback

        return self

    @log_calls
    def __getattr__(self, fn_name):
        self.require_login()  # all automatic calls require a login
        return api_key_injector(getattr(self.wobble_server, fn_name),
                                self.api_key)

    @log_calls
    def connect(self, user_name, user_password):
        self.api_key = self.user_login(user_name, user_password)
        return self

    @log_calls
    def user_login(self, email, password):
        result = self.wobble_server.user_login(email=email.lower(),
                                               password=password)
        return result['apikey']

    ### helper functions ###
    def archive_topic(self, topic_id):
        """Shorthand for topic_set_archived(archived=1)."""
        return self.topic_set_archived(topic_id=topic_id, archived=1)

    def require_login(self):
        if not self.is_loged_in():
            raise LoginRequiredException("Did you forget to call .connect()?")

    def is_loged_in(self):
        return self.api_key is not None

    def __str__(self):
        return "<WobbleService({})>".format(self.api_endpoint)
