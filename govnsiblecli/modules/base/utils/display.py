import logging

def mod_info():
    return {
    'module_name': 'logging',
    'module_type': 'base',
    'module_desc': 'Base module for initting logging'
    }

def init_logger(name):
    formatter = logging.Formatter(fmt='################\n%(asctime)s - %(levelname)s - %(module)s\n%(message)s\n#####################\n')

    handler = logging.StreamHandler()
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    return logger


def get_logger(name):
    return logging.getLogger(name)
