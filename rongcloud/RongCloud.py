from rongcloud.Chatroom import Chatroom
from rongcloud.Conversation import Conversation
from rongcloud.Group import Group
from rongcloud.Message import Message
from rongcloud.Sensitive import Sensitive
from rongcloud.User import User


class RongCloud:
    class _HostUrl:
        def __init__(self, host_url):
            self.host_list = host_url.split(',')
            self.now = 0
            self.times = 0

        def reset_times(self):
            self.times = 0

        def add_times(self):
            self.times = self.times + 1

        def get_times(self):
            return self.times

        def get_url(self):
            return self.host_list[self.now]

        def switch_url(self):
            if self.now < len(self.host_list) - 1:
                self.now = self.now + 1
            else:
                self.now = 0

    def __init__(self, app_key, app_secret, host_url='http://api.cn.ronghub.com'):
        self.app_key = app_key
        self.app_secret = app_secret
        self.host_url = self._HostUrl(host_url)

    def get_user(self):
        return User(self)

    def get_message(self):
        return Message(self)

    def get_group(self):
        return Group(self)

    def get_conversation(self):
        return Conversation(self)

    def get_chatroom(self):
        return Chatroom(self)

    def get_sensitive(self):
        return Sensitive(self)