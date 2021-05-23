from . import ExecutorBase

MOD_INFO = {
    'module_name': 'local',
    'module_type': 'executor',
    'module_description': 'Local executor to execute commands locally'
}

def mod_info():
    return MOD_INFO

class LocalExecutor(ExecutorBase):
    def __init__(self,*args):
        super(LocalExecutor, self).__init__('local')
        self.connection_type = 'local'

    def _execute_task(self, module_name):
        pass
