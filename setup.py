import json

default_path = '~/.config/'
default_operation = 'ln -s'

config_json = open('config.json')
config = json.load(config_json)

print(config)
