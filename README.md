# slack-cli

Send message to Slack channel in cli as a Slack app.

## Prerequisites

- Python 3.6+
- Slack App OAuth Access Token

## Usage

```
$ slack --help
Usage: slack [OPTIONS] [SOMETHING]...

Options:
  -t, --target TEXT      Post message to target channel
  -u, --user TEXT        Send as user [USER]
  -c, --config FILENAME  Path to config file
  --help                 Show this message and exit.
```

## Installation

### Pip

```
$ pip3 install git+ssh://git@github.com/reverbc/slack-cli.git
```

### Pipsi (https://github.com/mitsuhiko/pipsi)

```
$ pipsi install --python python3.6 git+ssh://git@github.com/reverbc/slack-cli.git
```

## How-To

1. Copy `slack-cli.json.template` to `~/.slack-cli.json`
1. Create Slack App
    1. Go to https://api.slack.com/apps?new_app=1 to create a new app
    1. After creation, go directly to *Features/OAuth & Permissions* page
    1. Add the following scopes
        - `channels:read`
        - `chat:write:bot`
    1. Install Slack app to your workspace
1. Under *Features/OAuth & Permissions* page, copy the OAuth Access Token and put to `TOKEN` of `~/.slack-cli.json`
1. (Optional) Limit available channels in `CHANNELS` of `~/.slack-cli.json`
1. Say hello, world
```
$ slack hello, world!
```
