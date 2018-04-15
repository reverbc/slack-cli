# -*- coding: utf-8 -*-
from setuptools import setup


def get_file(file, split=True):
    try:
        with open(file) as requirements_file:
            content = requirements_file.read().strip()
            return content.split('\n') if split else content
    except IOError:
        return None


setup(
    name='Slack-CLI',
    version='0.1',
    description='Slack CLI',
    author='Reverb Chu',
    author_email='reverbc@me.com',
    url='https://github.com/reverbc/slack-cli',
    install_requires=get_file('requirements.txt'),
    packages=['slack_cli'],
    entry_points='''
        [console_scripts]
        slack=slack_cli.cli:say
    '''
)
