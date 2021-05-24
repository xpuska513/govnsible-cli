import importlib

from . import ExecutorBase

MOD_INFO = {
    'module_name': 'local',
    'module_type': 'executor',
    'module_description': 'Local executor to execute commands locally'
}

def mod_info():
    return MOD_INFO

class GovnsibleExecutor(ExecutorBase):
    def __init__(self,*args):
        super(GovnsibleExecutor, self).__init__('local')
        self.connection_type = 'local'

    def execute_task(self, module_name, module_params):
        module = [item for item in self.module_list if item['mod_name'] == module_name]
        print(module)
        mod_py_name = module[0].get('mod_py_name')
        print(mod_py_name)
        dynamic_module = importlib.import_module(mod_py_name)
        mod_handler = dynamic_module.GovnsibleModule(module_params)
        mod_handler.execute_task()
        result = mod_handler.result
        return result
