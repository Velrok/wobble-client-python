# -*- coding: utf-8 -*-
import logging
import jsonrpclib


def requires_login(fn):
    def wrapper(*args):
        # TODO: check if logged in, else throw error

        # call method
        fn(*args)
    return wrapper


class WobbleService(object):
    """WobbleService"""

    def log_calls(fn):
        def wrapper(self, *args):
            result = fn(self, args)
            logging.debug("{obj}.{method}{params} ->\t{result}".format(
                obj=self, method=fn.func_name, params=args, result=result))
            return result
        return wrapper

    def __init__(self, api_endpoint='http://wobble.moinz.de/api/endpoint.php'):
        super(WobbleService, self).__init__()
        self.wobble_server = jsonrpclib.Server(api_endpoint)
        self.logger = None

    @log_calls
    def connect(self, user_name_or_api_key, user_password=None):
        if user_password is None:
            # only one parameter so its the api key
            self.api_key = user_name_or_api_key
        else:
            # we have user name and password
            self.api_key = self.user_login(user_name_or_api_key, user_password)


    def wobble_api_version(self):
        return self.wobble_server.wobble.api_version()

    def version_compatebility_check(self):
        version = self.wobble_api_version()
        major, minor, patch = map(int, version.split('.'))
        return (major <= 0 or minor <= 6)

    @log_calls
    @requires_login
    def topics_list(self, archived=False):
        pass

    @log_calls
    @requires_login
    def topics_search(self, query):
        pass

    @log_calls
    @requires_login
    def topics_create(self, topic_id):
        # params => id
        pass

    @log_calls
    @requires_login
    def topic_get_details(self, topic_id):
        # params => id
        pass

    @log_calls
    @requires_login
    def topic_add_user(self, topic_id, contact_id):
        pass

    @log_calls
    @requires_login
    def topic_remove_user(self, topic_id, contact_id):
        pass

    @log_calls
    @requires_login
    def topic_set_archived(self, topic_id, archived):
        # archived => Boolean(0,1)
        pass

    @log_calls
    @requires_login
    def topic_remove_message(self, topic_id, post_id):
        # params => message_id
        pass

    @log_calls
    @requires_login
    def post_create(self, topic_id, post_id, parent_post_id, intended_reply):
        # intended_reply => Boolean(0,1)
        pass

    @log_calls
    @requires_login
    def post_edit(self, topic_id, post_id, content, revision_no):
        # revision_no => Number of current revision
        pass

    @log_calls
    @requires_login
    def post_delete(self, topic_id, post_id):
        pass

    @log_calls
    @requires_login
    def post_read(self, topic_id, post_id, read):
        # read => Boolean
        pass

    @log_calls
    @requires_login
    def post_change_lock(self, topic_id, post_id, lock):
        # lock => Boolean(0,1)
        pass

    @log_calls
    @requires_login
    def user_get(self):

        pass

    @log_calls
    @requires_login
    def user_get_id(self):

        pass

    @log_calls
    @requires_login
    def user_register(self, email, password):

        pass

    @log_calls
    @requires_login
    def user_change_name(self, new_name):

        pass

    @requires_login
    def user_change_password(self, new_password):
        pass

    @log_calls
    @requires_login
    def user_login(self, email, password):
        pass

    @log_calls
    @requires_login
    def user_signout(self):
        pass

    @log_calls
    @requires_login
    def get_notifications(self, next_timestamp=None):
        pass

    @log_calls
    @requires_login
    def user_get_contacts(self):
        pass

    @log_calls
    @requires_login
    def user_add_contact(self, contact_email):
        pass

    @log_calls
    @requires_login
    def user_remove_contact(self, contact_id):
        pass

    def __str__(self):
        return "<WobbleService({})>".format(self.api_endpoint)
