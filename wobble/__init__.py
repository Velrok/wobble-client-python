# -*- coding: utf-8 -*-

import jsonrpclib


def requires_login(fn):
    def wrapper(*args):
        # TODO: check if logged in, else throw error

        # call method
        fn(*args)
    return wrapper


class WobbleService(object):
    """WobbleService"""
    def __init__(self, api_endpoint = 'http://wobble.moinz.de/api/endpoint.php'):
        super(WobbleService, self).__init__()
        wobble_server = jsonrpclib.Server(api_endpoint)

    def wobble_api_version(self):
        # method_name = 'wobble.api_version'
        pass

    @requires_login
    def topics_list(self, archived=False):
        pass

    @requires_login
    def topics_search(self, query):
        pass

    @requires_login
    def topics_create(self, topic_id):
        # params => id
        pass

    @requires_login
    def topic_get_details(self, topic_id):
        # params => id
        pass

    @requires_login
    def topic_add_user(self, topic_id, contact_id):
        pass

    @requires_login
    def topic_remove_user(self, topic_id, contact_id):

        pass

    @requires_login
    def topic_set_archived(self, topic_id, archived):
        # archived => Boolean(0,1)
        pass

    @requires_login
    def topic_remove_message(self, topic_id, post_id):
        # params => message_id
        pass

    @requires_login
    def post_create(self, topic_id, post_id, parent_post_id, intended_reply):
        # intended_reply => Boolean(0,1)
        pass

    @requires_login
    def post_edit(self, topic_id, post_id, content, revision_no):
        # revision_no => Number of current revision
        pass

    @requires_login
    def post_delete(self, topic_id, post_id):
        pass

    @requires_login
    def post_read(self, topic_id, post_id, read):
        # read => Boolean
        pass

    @requires_login
    def post_change_lock(self, topic_id, post_id, lock):
        # lock => Boolean(0,1)
        pass

    @requires_login
    def user_get(self):

        pass

    @requires_login
    def user_get_id(self):

        pass

    @requires_login
    def user_register(self, email, password):

        pass

    @requires_login
    def user_change_name(self, new_name):

        pass

    @requires_login
    def user_change_password(self, new_password):
        pass

    @requires_login
    def user_login(self, email, password):
        pass

    @requires_login
    def user_signout(self):
        pass

    @requires_login
    def get_notifications(self, next_timestamp=None):
        pass

    @requires_login
    def user_get_contacts(self):
        pass

    @requires_login
    def user_add_contact(self, contact_email):
        pass

    @requires_login
    def user_remove_contact(self, contact_id):
        pass
