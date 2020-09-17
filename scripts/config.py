#!/usr/bin/python3
import yaml

class Config():
    def __init__(self):
        self.path = '../config.yaml'
        self._config = self.load()

    def load(self):
        with open(self.path) as file:
            return yaml.load(file, Loader=yaml.FullLoader)

    def get(self, key):
        if key in self._config:
            return self._config[key]
        else:
            return 'Sorry, the key {} doesn\'t exist in config.yaml.'.format(key)

    def update(self, key, value):
        self._config[key] = value
        with open(self.path, 'w') as file:
            yaml.dump(self._config, file, sort_keys=True)
            return self._config


