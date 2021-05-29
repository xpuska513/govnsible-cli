import os

import govnsiblecli.modules.base.utils.display
from shlex import split
from govnsiblecli.modules import ModuleBase


logger = govnsiblecli.modules.base.utils.display.get_logger('root')

MOD_INFO = {
    'module_name': 'file',
    'module_type': 'general',
    'module_desc': 'Module to manipulate files'
}


def mod_info():
    return MOD_INFO


class GovnsibleModule(ModuleBase):
    def __init__(self,params):
        super(GovnsibleModule, self).__init__()
        self.params = params
        self.result = None

    def execute_task(self):
        task_params = self.params
        type = task_params.get('type')
        path = task_params.get('path')
        mode = task_params.get('mode')
        owner = task_params.get('owner')
        group = task_params.get('group')
        state = task_params.get('state')

        if type == 'directory':
            if state == 'present':
                try:
                    os.mkdir(path)
                    return {'state': 'changed', 'path': path}
                except OSError:
                    return "Error"
            if state == 'absent':
                try:
                    os.rmdir(path)
                except OSError:
                    return "Error"
        if not type:
            if state == 'present':
                os.mknod(path)
                return {'state': 'changed', 'path': path}
            if mode:
                os.chmod(path,mode)
                return {'state': 'changed', 'path': path}
            if owner and group:
                os.chown(path,owner,group)
                return {'state': 'changed', 'path': path}
