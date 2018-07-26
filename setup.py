# setup.py - creates config.json file required to run bot

import json

config = {
    "bot_token": "BOT_TOKEN"
}

f = open('config.json', 'w')
f.write(json.dumps(config, indent=2))
f.close