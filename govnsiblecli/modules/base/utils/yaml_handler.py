import yaml
import jinja2

MOD_INFO = {
    'module_name': 'yaml_handler',
    'module_type': 'base',
    'module_desc': 'Base module for handling yaml files'
}

def mod_info():
    return MOD_INFO

def pre_process_jinja_exprs(filepath):
    pass


def load_file(filepath):
    file_desc = open(filepath, 'r')
    return yaml.load(file_desc, Loader=yaml.FullLoader)

