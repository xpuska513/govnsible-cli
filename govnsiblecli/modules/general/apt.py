import apt
import sys

import govnsiblecli.modules.base.utils.display
from shlex import split
from govnsiblecli.modules import ModuleBase


logger = govnsiblecli.modules.base.utils.display.get_logger('root')

MOD_INFO = {
    'module_name': 'apt',
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
        package_name = task_params.get('name')
        state = task_params.get('state')
        cache = apt.cache.Cache()
        cache.update()
        cache.open()

        pkg = cache[package_name]
        if pkg.is_installed:
            self.result = 'Package is installed'
        if state == 'present':
            pkg.mark_install()
            try:
                cache.commit()
            except Exception as arg:
                logger.error(sys.stderr, f"Package install failed: {arg}")
                self.result = 'Failed'
            self.result = 'Success'
        if state == 'absent':
            pkg.mark_delete()
            try:
                cache.commit()
            except Exception as arg:
                logger.error(sys.stderr, f"Package install failed: {arg}")
                self.result = 'Failed'
            self.result = 'Success'
        self.result = 'No action provided'
