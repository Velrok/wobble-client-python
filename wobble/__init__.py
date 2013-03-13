class WobbleService(object):
    """WobbleService"""
    def __init__(self, api_key, api_endpoint="http://wobble.moinz.de/endpoint.php"):
        super(WobbleService, self).__init__()
        self.api_key = api_key
        self.api_endpoint = api_endpoint

    def check_version(self):
        pass

    def list_inbox(self):
        "Returns a list of all topics in the users inbox."
        pass

    def list_archive(self):
        "Returns a list of all topics in the users inbox."
        pass

    def list_unread_topics(self):
        pass

    def list_contacts(self):
        pass

    def list_comment_authors(self, topic_id, comment_id):
        pass

    def list_comments(self, topic_id):
        pass

    def add_contact(self):
        pass

    def add_participant_to_topic(self, participant_id, topic_id):
        pass

    def search(self, query):
        pass

    def archive_topic(self, topic_id):
        pass

    def create_topic(self, content):
        pass

    def fetch_topic_content(self, topic_id):
        pass

    def fetch_topic_participants(self, topic_id):
        pass

    def create_comment(self, topic_id, content):
        pass

    def replay_to_comment(self, topic_id, comment_id, content):
        pass
