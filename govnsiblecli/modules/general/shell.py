import subprocess

import govnsiblecli.modules.base.utils.display
from shlex import split
from govnsiblecli.modules import ModuleBase


logger = govnsiblecli.modules.base.utils.display.get_logger('root')

MOD_INFO = {
    'module_name': 'shell',
    'module_type': 'general',
    'module_desc': 'Module to execute shell commands'
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
        shell_command = task_params.get('command')
        command = split(shell_command)
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        self.result = result.stdout
