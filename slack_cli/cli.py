import os
import json
import pathlib
import sys

import click

from .slack import Slack


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


@click.command()
@click.option('--target', '-t', type=str, default='sandbox', help='Post message to target channel')
@click.option('--user', '-u', type=str, default=None, help='Send as user [USER]')
@click.option('--config', '-c', 'config_obj', type=click.File(), help='Path to config file')
@click.argument('something', nargs=-1)
def say(something, target, user, config_obj):
    try:
        if config_obj is None:
            with open(os.path.join(str(pathlib.Path.home()), '.slack-cli.json'), encoding='utf-8') as config_obj:
                config = json.load(config_obj)
        else:
            config = json.load(config_obj)

        assert config
    except Exception as ex:  # pylint: disable=W0703
        eprint(f'Failed to read config file:\n{ex}')
        exit(1)

    slack = Slack(token=config['TOKEN'], channels=config['CHANNELS'] if 'CHANNELS' in config else None, username=user)
    slack.send_message(' '.join(something), channel=target)


if __name__ == '__main__':
    say()  # pylint: disable=E1120
