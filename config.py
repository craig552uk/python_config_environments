# -*- coding: utf-8 -*-
#
# Author: Craig Russell <craig@craig-russell.co.uk>
#
# Examples:
#
# Set environment like
# >>> config.set_test()
#
# Test environment like
# >>> config.is_development()
# True
#
# Get config for current environment
# >>> config.load()
# {'environment': 'development'}
#
# Get config for specified environment
# >>> config.load(environment='test')
# {'environment': 'test'}


import os
import yaml # pip install pyyaml
import path # pip install path.py


def set_test():
    os.environ['ENVIRONMENT'] = "TEST"


def set_production():
    os.environ['ENVIRONMENT'] = "PRODUCTION"


def set_development():
    os.environ['ENVIRONMENT'] = "DEVELOPMENT"


def is_test():
    return os.environ.get('ENVIRONMENT', '') == "TEST"


def is_production():
    return os.environ.get('ENVIRONMENT', '') == "PRODUCTION"


def is_development():
    if not is_test() and not is_production():
        set_development()
    return os.environ.get('ENVIRONMENT', '') == "DEVELOPMENT"


def get_environment():
    if not os.environ.get('ENVIRONMENT'):
        set_development()
    return os.environ.get('ENVIRONMENT')


def load(environment=None):

    def _load_config_file(file_path):
        f = open(file_path, 'r')
        config = yaml.safe_load(f)
        f.close()
        if not config:
            return {}
        return config

    if environment in ['test', 'TEST', 'Test', 'T', 't']:
        set_test()

    if environment in ['production', 'PRODUCTION', 'Production', 'live', 'LIVE', 'Live', 'P', 'p', 'L', 'l']:
        set_production()

    if environment in ['development', 'DEVELOPMENT', 'Development', 'dev', 'DEV', 'Dev', 'D', 'd']:
        set_development()
    
    if is_test():
        return _load_config_file(path.path("config/test.yaml").abspath())

    if is_production():
        return _load_config_file(path.path("config/production.yaml").abspath())

    if is_development():
        return _load_config_file(path.path("config/development.yaml").abspath())
