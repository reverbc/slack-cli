# -*- coding: utf-8 -*-
from slacker import Slacker


class Slack(object):
    def __init__(self, token, channels=None, username=None, icon_url=None):
        self.slack = Slacker(token)
        self.username = username
        self.icon_url = icon_url
        self.channels = channels if channels else self.list_channels()

    def list_channels(self):
        return [channel['name'] for channel in self.slack.channels.list().body['channels'] if not channel['is_archived']]

    def send_message(self, message, channel):
        if channel not in self.channels:
            raise AttributeError(f'Channel [{channel}] is not available')

        self.slack.chat.post_message(
            f'#{channel}',
            message,
            username=self.username,
            icon_url=self.icon_url)

    def __getattr__(self, channel):
        if channel in self.channels:
            return lambda x: self.send_message(x, channel=channel)
        raise AttributeError(f'Channel [{channel}] is not available')
