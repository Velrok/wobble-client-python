# -*- coding: utf-8 -*-
import logging
import jsonrpclib


class LoginRequiredException(Exception):
    pass


class WobbleService(object):
    """WobbleService"""

    def requires_login(fn):
        def requires_login_decorator(self, *args):
            if not self.is_loged_in():
                raise LoginRequiredException("Did you forget to call .connect()?")
            return fn(self, *args)
        return requires_login_decorator

    def log_calls(fn):
        def log_calls_decorator(*params):
            self = params[0]
            args = params[1:]

            logging.debug("{obj}.{method}{params}".format(
                obj=self, method=fn.func_name, params=args))

            result = fn(*params)

            logging.debug("{obj}.{method}{params} ->\t{result}".format(
                obj=self, method=fn.func_name, params=args, result=result))

            return result

        return log_calls_decorator

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
        if exception:
            logging.error(exception)
            logging.error(error)
            logging.error(traceback)

        self.user_signout()
        return self

    @log_calls
    def connect(self, user_name, user_password):
        self.api_key = self.user_login(user_name, user_password)
        return self

    def is_loged_in(self):
        return self.api_key is not None

    def wobble_api_version(self):
        return self.wobble_server.wobble.api_version()

    def version_compatebility_check(self):
        version = self.wobble_api_version()
        major, minor, patch = map(int, version.split('.'))
        return (major <= 0 or minor <= 6)

    @requires_login
    @log_calls
    def topics_list(self, archived=False):
        pass

    @requires_login
    @log_calls
    def topics_search(self, query):
        pass

    @requires_login
    @log_calls
    def topics_create(self, topic_id):
        # params => id
        pass

    @requires_login
    @log_calls
    def topic_get_details(self, topic_id):
        # params => id
        result = self.wobble_server.topic_get_details(id=topic_id,
                                                      apikey=self.api_key)
        return result

    @requires_login
    @log_calls
    def topic_add_user(self, topic_id, contact_id):
        pass

    @requires_login
    @log_calls
    def topic_remove_user(self, topic_id, contact_id):
        pass

    @requires_login
    @log_calls
    def topic_set_archived(self, topic_id, archived):
        # archived => Boolean(0,1)
        pass

    @requires_login
    @log_calls
    def topic_remove_message(self, topic_id, post_id):
        # params => message_id
        pass

    @requires_login
    @log_calls
    def post_create(self, topic_id, post_id, parent_post_id, intended_reply):
        # intended_reply => Boolean(0,1)
        pass

    @requires_login
    @log_calls
    def post_edit(self, topic_id, post_id, content, revision_no):
        # revision_no => Number of current revision
        pass

    @requires_login
    @log_calls
    def post_delete(self, topic_id, post_id):
        pass

    @requires_login
    @log_calls
    def post_read(self, topic_id, post_id, read):
        # read => Boolean
        pass

    @requires_login
    @log_calls
    def post_change_lock(self, topic_id, post_id, lock):
        # lock => Boolean(0,1)
        pass

    @requires_login
    @log_calls
    def user_get(self):
        pass

    @requires_login
    @log_calls
    def user_get_id(self):
        pass

    @requires_login
    @log_calls
    def user_register(self, email, password):
        self.wobble_server.user_register(email, password)

    @requires_login
    @log_calls
    def user_change_name(self, new_name):
        pass

    @requires_login
    def user_change_password(self, new_password):
        pass

    @log_calls
    def user_login(self, email, password):
        result = self.wobble_server.user_login(email=email.lower(),
                                               password=password)
        return result['apikey']

    @requires_login
    @log_calls
    def user_signout(self):
        return self.wobble_server.user_signout(apikey=self.api_key)

    @requires_login
    @log_calls
    def get_notifications(self):
        result = self.wobble_server.get_notifications(next_timestamp=self.last_notification_timestamp,
                                                      apikey=self.api_key)
        self.last_notification_timestamp = result['next_timestamp']
        return result['messages']

    @requires_login
    @log_calls
    def user_get_contacts(self):
        pass

    @requires_login
    @log_calls
    def user_add_contact(self, contact_email):
        pass

    @requires_login
    @log_calls
    def user_remove_contact(self, contact_id):
        pass

    def __str__(self):
        return "<WobbleService({})>".format(self.api_endpoint)
